from . import views
from django.urls import path

urlpatterns = [# localhost:8000/users
    path('', views.home),
]
