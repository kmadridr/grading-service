from fastapi import FastAPI
from graphene import ObjectType, String, Schema

app = FastAPI()

class Query(ObjectType):
    hello = String()

    def resolve_hello(self, info):
        return "Hello, world!"

schema = Schema(query=Query)

@app.post("/graphql")
async def graphql(query: str):
    result = schema.execute(query)
    return result.to_dict()
