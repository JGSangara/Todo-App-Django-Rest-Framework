## Todo App REST API

This is a REST API for a Todo application, built with Django and Django REST Framework.

![Screenshot of the application](https://github.com/JGSangara/Resources/blob/main/Todo-App-Django-Rest-Framework.png)


## 🚀 Features

- User registration and authentication
- Password reset functionality
- CRUD operations for tasks

## 🛠️ Prerequisites

- Python 3.9 or higher
- Django
- Django REST Framework

## 📝 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation

1. Clone the repository:
```sh
git clone https://github.com/JGSangara/todo_app_restAPI
```

2. Navigate to the project directory:
```sh
cd todo_app_restAPI
```

3. Install the requirements:
```sh
pip install -r requirements.txt
```

4. Run migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:
```sh
python manage.py runserver
```

## 🧪 Running Tests

To run tests, execute the following command:
```sh
python manage.py test
```

## 🛠️ Tech Stack

**Backend Framework:**
- Django 5.2.10
- Django REST Framework 3.16.1

**Authentication:**
- djangorestframework-simplejwt 5.5.1 (JWT Token Authentication)
- Token blacklisting for secure logout

**API Documentation:**
- drf-yasg 1.21.11 (Swagger/OpenAPI specification)

**Additional Libraries:**
- django-cors-headers 4.9.0 (Cross-Origin Resource Sharing)
- django-filter 25.2 (Filtering and search capabilities)
- django-environ 0.12.0 (Environment variable management)
- Pillow 12.1.0 (Image processing)
- PyJWT 2.10.1 (JSON Web Token implementation)

**Database:**
- SQLite (Development)
- PostgreSQL ready (Production)

**Python Version:**
- Python 3.9+

## 🤝 Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
