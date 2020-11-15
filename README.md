# PBO2020-1908561091-UTS

# Installasi
 ``` python
 pip install django
 virtualenv venv
 pip install mysqlclient
 
 . venv/Scripts/activate
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
 ```
 
 # Sesuaikan Database 
 myproject/settings.py
 ```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
 ```
