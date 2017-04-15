# papersplease
Web application to handle conference papers collection

## Deployment

 * Dependencies:
    * python 2 / 3
    * Django >= 1.7
    * psycopg2, only if you use postgresql database

 * Copy the file local\_settings.py.example to local\_settings.py and
   change the default configuration. You should change the SECRET\_KEY and
   configure the database.

 * Run the database migrations:
```
python manage.py migrate
```

 * Create an admin user:
```
python manage.py createsuperuser
```

 * Deploy it in your web server: https://docs.djangoproject.com/en/1.7/howto/deployment/
