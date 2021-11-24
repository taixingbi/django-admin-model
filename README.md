
### run aws ubuntu 18.04
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04

```
python3 -m venv my_env
source my_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### run migrate
##### packaging up your model changes
```
python manage.py makemigrations 
```

##### applying those to your database.
```
python manage.py migrate --run-syncdb 
```

##### create supersuer
```
python manage.py createsupersuer
```

### run local
```
python manage.py runserver 0.0.0.0:8083
```
