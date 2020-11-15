# PBO2020-1908561091-UTS

# Installasi
 ``` python
 pip install django
 ```
 ``` python
 virtualenv venv
 ```
 ``` python
 pip install mysqlclient
 ```
 ``` python
 . venv/Scripts/activate
 ```
 ``` python
 python manage.py makemigrations
 ```
 ``` python
 python manage.py migrate
 ```
 ``` python
 python manage.py runserver
 ```
 
 # Sesuaikan Database 
 myproject/settings.py
 ``` python
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
