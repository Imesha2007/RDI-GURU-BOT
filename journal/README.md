# Trading Journal (Django)

A simple trading journal web app where users can sign up, log in, and manage their trades (CRUD) with a dashboard for basic stats.

## Requirements
- Python 3.13+

## Setup

```
# In project root
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

If the built-in venv is unavailable, you can use virtualenv:
```
python3 -m pip install --break-system-packages virtualenv
python3 -m virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Run
```
cd journal
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Open http://localhost:8000

## Admin (for testing)
Create an admin user:
```
python manage.py createsuperuser
```

In this environment, a default admin may be set to:
- username: `admin`
- password: `adminpass`

## Features
- User auth (login, logout, signup)
- Trades CRUD (symbol, side, qty, entry/exit price & time, notes)
- Dashboard with trade count, realized count, total PnL, win rate
- Basic styling and navigation

## App Structure
- Project: `journal/`
- App: `trades/`
- Templates: `templates/`
- Static: `static/`

## Notes
- Uses SQLite by default. Switch to Postgres/MySQL in `journal/settings.py` for production.
- Set `DEBUG=False` and configure `ALLOWED_HOSTS` for deployment.
