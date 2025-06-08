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