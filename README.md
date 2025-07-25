# OGA Database Archive

This repository contains the archived source code for the **Only Good Antibodies (OGA)** website and e‑learning module. It is intended as a reference implementation to reproduce our analyses and training materials. Sensitive keys and media have been stripped; follow the instructions below to configure and run locally.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Configuration](#configuration)  
   - [Database Setup](#database-setup)  
4. [Running the Application](#running-the-application)  
5. [Project Structure](#project-structure)  
6. [Contributing](#contributing)    
7. [Contact](#contact)  

---

## Project Overview

The OGA website provides:

- A browsable, searchable database of genes and associated antibodies  
- Detailed experiment records (WB, IP, ICC‑IF, FC)  
- User‑driven contact and resource pages  
- An integrated e‑learning “Academy” module with lessons, quizzes, and certificate generation  

This archive excludes production credentials, media uploads, and static build artifacts. It serves as a reproducible snapshot for research and development.

---

## Features

- **Django‑based backend** (Django 5.1)  
- **Core app**: gene/antibody database, search, filters, PDF citation  
- **Academy app**: lessons, sections, progress tracking, quizzes, certificates  
- **Authentication**: Django allauth + social (Google)  
- **Rich‑text**: CKEditor for lesson content  
- **Frontend**: Bootstrap 5 + custom CSS  

---

## Getting Started

### Prerequisites

- Python 3.10+  
- Git  
- [Node.js & npm](https://nodejs.org/) (for frontend asset builds, if customizing)  
- A Unix‑like shell (Linux, macOS, WSL)

### Installation

```bash
# 1. Clone this archive
git clone git@github.com:onlygoodantibodies/OGA_database_archive.git
cd OGA_database_archive

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate



# OGA Database Archive

A public archive of the **Only Good Antibodies (OGA)** website and e‑learning module code, intended to accompany scientific publications for reproducibility and transparency.

## Features

* **Core App (`core/`)**: Gene & antibody database with filters, search, and experiment imagery.
* **Academy App (`academy/`)**: E‑learning modules, progress tracking, quizzes, and PDF certificate generation.
* **Django Project (`OGA_website/`)**: Central settings, URL routing, static/media configuration.
* **Responsive Design**: Mobile‑first CSS, accessible layouts, and cookie consent banner.
* **Third‑Party Integration**: Django Allauth for authentication, CKEditor for rich text, WhiteNoise for static files.

---

## Configuration

1. **Copy the example environment file** and edit secrets:

   ```bash
   cp .env.example .env
   ```

2. **Open `.env`** and set:

   ```dotenv
   SECRET_KEY=your_django_secret_key
   DEBUG=False
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3    # or your Postgres/MySQL URL
   EMAIL_HOST_USER=you@example.com
   EMAIL_HOST_PASSWORD=your_smtp_password
   ```

3. **(Optional) Configure social login** credentials in `.env`:

   ```dotenv
   SOCIAL_GOOGLE_CLIENT_ID=...
   SOCIAL_GOOGLE_SECRET=...
   ```

---

## Database Setup

```bash
# Create migrations based on models
python manage.py makemigrations

# Apply migrations to your database
python manage.py migrate

# Create a Django superuser for admin access
python manage.py createsuperuser
```

---

## Running the Application

```bash
# Collect static assets into STATIC_ROOT
python manage.py collectstatic --noinput

# Start the development server
python manage.py runserver
```

* Public site: `http://127.0.0.1:8000/`
* E‑learning module: `http://127.0.0.1:8000/academy/`

---

## Project Structure

```
OGA_database_archive/
├── academy/               # E‑learning Django app
│   ├── migrations/        # Database migrations
│   ├── templates/academy/ # Academy templates
│   ├── static/academy/    # Academy CSS & JS
│   ├── models.py          # Lesson, Quiz, Certificate, Progress
│   └── views.py
├── core/                  # Public gene/antibody site
│   ├── migrations/        # Database migrations
│   ├── templates/core/    # Core templates
│   ├── static/core/       # CSS, images, scripts
│   ├── models.py          # Gene, Antibody, Experiment, Description
│   └── views.py
├── OGA_website/           # Django project settings & URLs
│   ├── settings.py        # Reads from .env
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3             # Default SQLite DB (ignored in prod)
├── requirements.txt       # Python dependencies
├── .env.example           # Sample environment variables
└── README.md              # This documentation
```

---

## Contributing

1. Fork this repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add awesome feature"
   ```
4. Push to your fork:

   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request against `onlygoodantibodies/OGA_database_archive:main`.

Please follow the existing code style and add tests for new functionality.

---

## Contact

For questions, issues, or collaboration:

* **Email**: [onlygoodantibodies@gmail.com](mailto:onlygoodantibodies@gmail.com)
* **GitHub**: [onlygoodantibodies](https://github.com/onlygoodantibodies)

> *This README was generated to accompany the OGA database and e‑learning code archive for reproducible research.*


# 3. Install Python dependencies
pip install -r requirements.txt
