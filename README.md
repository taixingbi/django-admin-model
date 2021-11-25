
### run aws ubuntu 18.04
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-18-04

```
python3 -m venv my_env
source my_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

##### packaging up your model changes
```
python manage.py makemigrations
python manage.py migrate
```


### run local
```
python manage.py runserver 0.0.0.0:8083
python manage.py runserver --noreload
```



