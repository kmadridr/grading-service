from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graphene import ObjectType, String, Schema, List, Field, Float, InputObjectType, Int, NonNull
from database.models import Course, Student, Enrollment

app = FastAPI()

# SQLAlchemy configuration
engine = create_engine("sqlite:///grades.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)

# GraphQL types
class CourseType(ObjectType):
    class Meta:
        description = "Course"
    
    id = String()
    name = String()

class EnrollmentType(ObjectType):
    class Meta:
        description = "Enrollment"

    student_id = Int()
    course_id = Int()
    grade = Float()

class Query(ObjectType):
    hello = String()
    courses = List(CourseType)
    enrollments = List(EnrollmentType)

    def resolve_hello(self, info):
        return "Hello, world!"

    def resolve_courses(self, info):
        session = SessionLocal()
        courses = session.query(Course).all()
        return courses

    def resolve_enrollments(self, info):
        session = SessionLocal()
        enrollments = session.query(Enrollment).all()
        return enrollments

class AddCourseInput(InputObjectType):
    name = Field(NonNull(String))

class AddCourseMutation(ObjectType):
    class Meta:
        description = "Add a new course"

    course = Field(CourseType)

    @staticmethod
    def mutate(root, info, input):
        session = SessionLocal()
        course = Course(name=input.name)
        session.add(course)
        session.commit()
        return AddCourseMutation(course=course)

class Mutation(ObjectType):
    add_course = AddCourseMutation.Field()

schema = Schema(query=Query, mutation=Mutation)

@app.post("/graphql")
async def graphql(query: str):
    result = schema.execute(query)
    return result.to_dict()

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:8080",
    # Add more allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)