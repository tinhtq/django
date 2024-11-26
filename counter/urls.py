from django.urls import path
from . import views

app_name = 'counter'  # Register the namespace
urlpatterns = [
    path('', views.index, name='index'),
]