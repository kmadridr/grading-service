# Grading Service

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Grading Service is an open-source backend service developed in Python using FastAPI and GraphQL. It aims to provide a reliable and cost-effective grading system for schools with limited budgets, enabling students to access and track their grades online.

## Features

- **Affordable Solution**: Grading Service offers a budget-friendly alternative for schools that require a grading system without the resources for custom development.
- **FastAPI**: Built with FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **GraphQL**: Utilizes GraphQL, a powerful query language for APIs, to provide flexible and efficient data retrieval and manipulation.
- **Secure Authentication**: Implements secure authentication mechanisms to ensure the privacy and confidentiality of student data.
- **Easy Integration**: Designed with ease of integration in mind, making it straightforward to incorporate Grading Service into existing school management systems.

## Getting Started

Follow these steps to get the Grading Service up and running on your local machine:

1. Clone the repository:

```shell
git clone https://github.com/your-username/grading-service.git
```

2. Navigate to the project directory:

```shell
cd grading-service
```

3. Create a Virtual Environment (recommended):
```shell
python -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```shell
pip install -r requirements.txt

```

5. Configure the application:
- Open the `config.py` file and customize the settings according to your environment.

6. Run the application:

```shell
uvicorn app.main:app --reload
```

7. Access the application:
- The Grading Service API is now available at `http://localhost:8000/`.
- Explore the API documentation and available endpoints using the interactive Swagger UI, accessible at `http://localhost:8000/docs`.

## Database Setup
The grading service uses SQLite as the default database, with SQLAlchemy as the ORM. 
The SQLite database file will be created automatically when you run the application.

## Contributing

Contributions are welcome and encouraged! To contribute to Grading Service, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

Please ensure that you adhere to the project's code style and guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

We would like to express our gratitude to all contributors who have made this project possible. Thank you for your support and dedication!



