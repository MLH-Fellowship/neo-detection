# neo-detection
Detecting Near-Earth Objects using NASA's API

## Installation
```sh
# Go into project directory
cd neo-detection

# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install all required packages (Django, Django REST Framework, dotenv, etc.) into virtual env
pip install -r requirements.txt

# Configure environment variables (instructions below)

# Sync database and apply migrations
python manage.py migrate

# Create an admin superuser with your desired username, email and password
python manage.py createsuperuser --username admin --email admin@example.com

# Run the server (default: 127.0.0.1:8000)
python manage.py runserver
```

## Environment Variables

Create a new `.env` file in root directory and use `.env.example` as a reference to provide the following environment variables:

```sh
DJANGO_SECRET_KEY=
NASA_API_KEY=
```

To generate a new Django secret key, run this in a Python virtual environment after dependencies have been installed.

```sh
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

[Sign up to generate a NASA API key](https://api.nasa.gov/#signUp).