requirements:

```bash
pip install django
pip install django-allauth
```

To create super user:

```bash
python manage.py createsuperuser
```

To run server:

```bash
python manage.py runserver
```

Once you have created a superuser,
run the server and go to the admin page at
http://localhost:8000/admin
then sign in with your credentials and access all information

to check the login page: 
http://localhost:8000/accounts/login

Then signup with google.
You will then be redirected to the homepage: