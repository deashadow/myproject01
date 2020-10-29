installation instructions---using python 3.8.5
pip install mysqlclient
pip install django


django-admin startproject myproject01
django-admin startapp example
python manage.py makemigrations example
python manage.py migrate
python manage.py shell
from example.models import Company
apple=Company(name='apple')
apple.save()