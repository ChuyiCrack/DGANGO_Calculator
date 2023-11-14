from . import views
from django.urls import path

urlpatterns=[
    path("", views.Calculator, name='calculator'),
    path('result/', views.Result,name='result')
]