# Django Research Center API

This is a Django-based REST API project designed to manage a research center. The project uses Django REST framework and various additional packages to provide robust functionality.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [API Documentation](#api-documentation)
6. [Contributing](#contributing)
7. [License](#license)

## Features

- Filtering capabilities with `django-filter`
- Comprehensive API documentation with `drf-yasg`

## Requirements

- Python 3.x
- The following Python packages, specified in `requirements.txt`:

```
asgiref==3.8.1
Django==5.0.6
django-filter==24.2
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
PyJWT==2.8.0
sqlparse==0.5.0
drf-yasg==1.21.7
```

## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ThomasPerez91/td-djangorestapi-PEREZ-THOMAS.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd td-djangorestapi-PEREZ-THOMAS
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

After installing the required packages, follow these steps to set up the database and run the server:

1. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`.

## API Documentation

The project uses \`drf-yasg\` to generate API documentation. Once the server is running, you can access the API documentation at:

- Swagger: \`http://127.0.0.1:8000/swagger/\`
- ReDoc: \`http://127.0.0.1:8000/redoc/\`

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (\`git checkout -b feature-branch\`).
3. Make your changes.
4. Commit your changes (\`git commit -am 'Add new feature'\`).
5. Push to the branch (\`git push origin feature-branch\`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Thank you for using the Django Research Center API! If you have any questions or encounter any issues, feel free to open an issue on the repository.
