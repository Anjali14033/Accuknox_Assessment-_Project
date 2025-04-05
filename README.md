# 🧠 Django Signals & Python Custom Class Assignment

This project includes:

1. Demonstrations to answer key questions about **Django Signals**.
2. A custom Python class called **Rectangle** implementing custom iteration behavior.

---

## 📦 Project Structure

signal_demo/ # Django Project Root ├── core/ # Django App for Signal Demos │ ├── models.py # Defines the Item model │ ├── signals.py # Signal handlers │ ├── apps.py # Registers signals ├── rectangle.py # Custom Rectangle class (Python) ├── manage.py # Django Management Script ├── db.sqlite3 # SQLite Database


---

## 🔧 Setup Instructions

### 1. Clone or Download the Repository

```bash
git clone https://github.com/Anjali14033/Accuknox_Assessment-_Project.git
cd signal_demo
```

### 2. Create a Virtual Environment

```bash
python -m venv env
# Activate the environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate
```

### 3. Install Requirements

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```


---

🧪 How to Run Django Signal Tests
The core/signals.py file contains logic that answers the following:

Question 1: Are Django signals synchronous?
✅ Yes. A time delay (time.sleep) in the signal handler proves the caller is blocked.

Question 2: Do Django signals run in the same thread?
✅ Yes. The main thread ID and signal handler thread ID are identical.

Question 3: Do Django signals run in the same database transaction?
✅ Yes. Using transaction.get_connection().in_atomic_block, both signal and caller are confirmed to share the same DB transaction.

---
🔍 To test: Run the server, then create an Item object from Django shell.

```bash
python manage.py shell
>>> from core.models import Item
>>> Item.objects.create(name="Signal Test")
```
---

🔁 Rectangle Class (Python Custom Class)
📄 File: rectangle.py

This class is initialized with length and width, and supports iteration.

✅ Features

```bash
{'length': <value>}, then {'width': <value>}
```

Example Usage:-

```bash
from rectangle import Rectangle

r = Rectangle(5, 3)
for dim in r:
    print(dim)

# Output:
# {'length': 5}
# {'width': 3}
```