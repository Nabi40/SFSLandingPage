### sfslandingpage

# 🚀 Django Docker Project

A containerized Django web application using PostgreSQL and environment-based configuration, perfect for scalable web development and deployment.

---

## 📄 Description

This project uses **Django 5**, **Docker**, and **PostgreSQL**, with configurations managed via a `.env` file. It includes email setup through Mailtrap and CORS handling for cross-origin requests — ideal for connecting to a frontend on port `3000`.

---

## ✨ Features

- 🐳 Dockerized development environment
- 🗃️ PostgreSQL database integration
- 🔐 Environment variables via `.env`
- 📧 Email backend with Mailtrap
- 🔄 Media directory management
- 🌐 CORS setup for frontend integration
- 🔧 Auto migration on container start

---

## 💻 Tech Stack

- **Backend:** Django 5.1.6
- **Database:** PostgreSQL 15
- **Containerization:** Docker, Docker Compose
- **Others:** Gunicorn, Pillow, Requests, Django REST Framework

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   cd SFS Website\source\web-django
   docker-compose up --build


#### ⚙️ changes are needed
- create an .env file following the .env.example with credientials


##### to export data from SFS.sql
   ```bash
   docker exec -i web-django-db-1 psql -U postgres -d SFS< SFS.sql 


##### error for having same id existing for exporting data from sfs.sql
   ```bash
   docker exec -it web-django-django-1 bash       #command 1

   python manage.py shell                         #command 2


   from django.db import connection               #command 3

   with connection.cursor() as cursor:
      cursor.execute("""
         SELECT setval(pg_get_serial_sequence('"django_admin_log"', 'id'),
                        (SELECT MAX(id) FROM "django_admin_log"));
      """)
