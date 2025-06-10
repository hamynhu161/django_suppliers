# Django Suppliers App

This is a simple Django web application to manage suppliers and products. It uses Bootstrap for styling and is built with Python and Django 5.

## 🚀 Features

- Manage suppliers and their details
- Manage products and link them to suppliers
- Admin interface included
- Bootstrap-styled interface
- Django-powered routing and templates

## 🛠️ Getting Started

### ✅ Requirements

- Python 3.10 or later
- Git
- pip (Python package manager)

### 🔧 Setup Instructions

1. **Clone the repository**
  
2. **Create and activate a virtual environment**:

    python -m venv venv </br>

    .\venv\Scripts\activate    (for Windows)
   
3. **Install dependencies**:
   
    pip install -r requirements.txt
   
4. **Create database tables needed by Django**:
   
    python manage.py migrate

5. **Run app**:

    python manage.py runserver

6. **To leave the virtual environment after using**:

   deactivate

### 🔧 Setup Instructions for using PostgreSQL as its database

1. **Install PostgreSQL**

    You can download it from https://www.postgresql.org/download/. </br>

    After installation, create a new database and user if needed.
  
2. **Install the PostgreSQL Python Driver inside Python virtual environment**:

    pip install psycopg2-binary
   
3. **Update the DATABASES configuration in settings.py**:
   
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_PostgreSQL_database_name',       
            'USER': 'your_PostgreSQL_username',           
            'PASSWORD': 'your_password',  
            'HOST': 'localhost',          
            'PORT': '5432',              
        }
    }
   
4. **Run database Migrations**:
   
    python manage.py migrate

5. **Run app**:

    python manage.py runserver

### 🔧  Test how app behaves in a real WSGI server  (simulate production locally)

1. **Install Waitress**

    pip install waitress

2. **Create server.py to lauch app with Waitress**

    from waitress import serve </br>
    from suppliers.wsgi import application </br>

    if __name__ == '__main__':      </br>
        print("Open browser at http://localhost:8080")      </br>
        print("Shut down server with 'control + c'")        </br>
        serve(application, host='127.0.0.1', port=8080)     </br>
  
3. **Start the server**:

    python server.py

### 🔧  Deploying to Render

For a complete step-by-step guide, check out Render’s official Django deployment documentation:

👉 [Render: Deploy a Django App](https://render.com/docs/deploy-django)

1. **Install required packages and update file requirements.txt**

    pip install gunicorn uvicorn whitenoise[brotli] dj-database-url psycopg2-binary </br>
    pip freeze > requirements.txt

2. **Update setting.py**

- Import helpers:

    import os </br>
    import dj_database_url </br>

- Configure database:

    DATABASES = {
        'default': dj_database_url.config(
            default='postgresql://postgres:Testaaja@localhost:5432/suppliers_db',
            conn_max_age=600
        )
    }
  
- Add WhiteNoise middleware:

    MIDDLEWARE = [
        'whitenoise.middleware.WhiteNoiseMiddleware',
        ...
    ]

- Configure static file handling:
    DEBUG = False </br>
    ALLOWED_HOSTS = ['*']    </br>
    -------
    if not DEBUG:
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

3. **Create a build script (this build script is run whenever a new deploy is initiated)**:

    #!/usr/bin/env bash
    set -o errexit

    pip install -r requirements.txt
    python manage.py collectstatic --noinput
    python manage.py migrate

4. **Create file render.yaml to tell Render to automatically create a PostgreSQL database, web service, use build.sh script to collect static files and run migrations and environment variables for security and flexibility**
