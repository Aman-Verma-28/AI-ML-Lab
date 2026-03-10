# AI-ML-Lab Project Skill

## Overview

This is a Django REST Framework project for a healthcare-related application. It provides API endpoints for YouTube integration, calendar/appointment booking, authenticated test views, and a plagiarism-checking (Turnitin-like) feature.

## Repository Structure

```
AI-ML-Lab/
├── README.md
├── aparna/                          # Python 3.8 virtual environment (committed to repo)
│   ├── bin/
│   ├── lib/
│   └── pyvenv.cfg
└── webscoket/                       # Note: directory name has a typo ("webscoket" instead of "websocket")
    └── websocket_ml/                # Django project root (manage.py lives here)
        ├── manage.py
        ├── db.sqlite3               # SQLite database
        ├── baseapp/                 # Main Django app
        │   ├── admin.py             # Registers HealthcareCentre and Referral models
        │   ├── apps.py              # App config (name: baseapp)
        │   ├── custom_auth.py       # Custom DRF authentication (secret key-based)
        │   ├── models.py            # Reminder, HealthcareCentre, Referral models
        │   ├── tests.py             # Empty test file
        │   ├── urls.py              # App-level URL routing
        │   ├── views.py             # API views (YoutubeAPI, CalendarAPI, TestView, TurnitinView)
        │   └── migrations/
        │       └── 0001_initial.py
        └── websocket_ml/            # Django project settings package
            ├── __init__.py
            ├── asgi.py
            ├── settings.py
            ├── urls.py              # Root URL config (includes baseapp.urls)
            └── wsgi.py
```

## Tech Stack & Dependencies

- **Python**: 3.8.10
- **Django**: 3.2
- **Django REST Framework** (djangorestframework)
- **requests** (used in TurnitinView for external API calls)
- **Database**: SQLite3 (default Django config)
- **No requirements.txt or pyproject.toml**: Dependencies must be installed manually via pip

## Setup & Running

### Install Dependencies

```bash
pip install django djangorestframework requests
```

### Run Migrations & Start Server

All Django management commands must be run from the `webscoket/websocket_ml/` directory:

```bash
cd webscoket/websocket_ml/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Create Superuser (for Django Admin)

```bash
cd webscoket/websocket_ml/
python manage.py createsuperuser
```

The Django admin is available at `/admin/` and has `HealthcareCentre` and `Referral` models registered.

## API Endpoints

All endpoints are served under the root URL (no prefix), defined in `baseapp/urls.py`:

| Endpoint             | Method | Auth Required | Description                                    |
|----------------------|--------|---------------|------------------------------------------------|
| `api/youtube/v1`     | GET    | No            | Returns YouTube-related data (singer, language, emotion) |
| `api/calendar/v1`    | GET    | No            | Returns appointment booking info (doctor, patient, meeting link) |
| `test`               | GET    | Yes           | Authenticated test endpoint (uses CustomAuthentication) |
| `turnitin/`          | POST   | No            | Plagiarism checking via external API (papersowl.com) |

## Models

- **Reminder**: Stores appointment reminders (time, doctor, patient, link, doctor_id)
- **HealthcareCentre**: Stores healthcare centre info (name, email)
- **Referral**: Generates and stores referral codes linked to a HealthcareCentre (auto-generated from email + hex token on save)

## Authentication

The project has a custom DRF authentication class in `baseapp/custom_auth.py`:
- Uses query parameters `username` and `secret_key`
- The secret key is hardcoded as a placeholder `<YourKey>` in the source
- Only the `TestView` endpoint uses this authentication

## Key Notes for Development

- The `webscoket/` directory name is intentionally misspelled in the repo — do not rename it without coordination
- The `aparna/` directory is a committed Python virtualenv — avoid modifying it; create your own venv instead
- There is no CI/CD pipeline, no linting configuration, no pre-commit hooks, and no test suite
- There is no `.gitignore` file — be careful not to commit generated files or local environment artifacts
- The `db.sqlite3` file is committed to the repo
- Django `SECRET_KEY` is hardcoded in settings.py (development only)
- `DEBUG = True` is set in settings.py
- `ALLOWED_HOSTS` is empty (only works for localhost)

## Running Tests

The test file (`baseapp/tests.py`) is empty. To run the Django test runner:

```bash
cd webscoket/websocket_ml/
python manage.py test
```
