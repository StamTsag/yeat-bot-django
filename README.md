# Yeat bot database & rest API recreated in Django

### Setup

- Create a virtual environment & enter it: `python -m venv .venv` then `. .venv/bin/activate`

- Install requirements: `pip install -r requirements.txt`

- Setup the database: `python manage.py makemigrations yeat_django` & `python manage.py migrate`

- Run the server: `python manage.py runserver 3000`, starts at port **3000**

- Visit `localhost:3000/guilds` to test the API out
