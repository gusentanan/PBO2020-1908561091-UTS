# PBO2020-1908561091-UTS

# Installasi
 -- pindah ke route direktori projek lalu jalankan command dibawah:
  ``` python
 virtualenv venv
 ```
  ``` python
 . venv/Scripts/activate
 ```
 ``` python
 pip install django
 ```
 ``` python
 pip install mysqlclient
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
