# 📰 NeoNews
NeoNews is a backend project designed to provide APIs for news management, including authorization, authentication, favorites functionality, and Swagger documentation. The project is containerized using Docker for easy deployment.

## 🚀 Features
News API: Endpoints for creating, retrieving, updating, and deleting news articles.
Authorization & Authentication: Secure access with JWT.
Favorites: API endpoints for managing favorite news articles.
Swagger: API documentation with Swagger UI.
Docker: Containerized application for easy deployment.

## 📁 Project Structure

neonews/
├── main/
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── neonews/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── news/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── news_images/
├── venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── pyvenv.cfg
├── .dockerignore
├── db.sqlite3
├── Dockerfile
├── manage.py
├── requirements.txt
├── rundocker.sh
├── runsite.sh

## 🛠️ Setup and Installation
Prerequisites
Docker
Docker Compose
Installation
1. Clone the repository:
git clone https://github.com/nasirovx/neonews.git
cd neonews
2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. Install the dependencies:
pip install -r requirements.txt
4. Run the application with Docker:
docker-compose up --build
