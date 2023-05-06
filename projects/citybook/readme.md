# Citybook project for internal exam

## How to start:
1) Create new virtual environment and install project dependencies

```
pip install -r requirements.txt
```

2) Make migrations
```
python manage.py migrate
```

3) Load fixtures
```
python manage.py loaddata fixtures/*
```

4) Run server
```
python manage.py runserver
```

Open admin panel [localhost:8000](http://localhost:8000/admin)

Default admin: admin

Default password: Pw123456

Open Swagger API documentation [localhost:8000/swagger/](http://localhost:8000/swagger/)
