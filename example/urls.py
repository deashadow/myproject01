from . import views
from django.urls import path

urlpatterns = [# localhost:8000/users
    path('', views.home),
    path('about', views.about),
    path('person/<id>', views.person),
]
