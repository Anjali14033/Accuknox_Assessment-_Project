<<<<<<< HEAD
# Django Signal Assignment

This project demonstrates:

- Synchronous signals
- Signal running in same thread
- Signal running within the same DB transaction
- Iterable Rectangle class in Python

## Setup Instructions

```bash
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

To test the signal:

```python
from core.models import Item
Item.objects.create(name="Test Signal")
```

## Rectangle Class Test

```bash
python rectangle.py
```

## GitHub Push Steps

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your_repo_url>
git push -u origin main
```
=======

