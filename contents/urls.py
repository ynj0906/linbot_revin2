from django.urls import path
from . import views

app_name = "app"
urlpatterns =[
    path('index',views.index),
    path('callback', views.callback),
]