from django.urls import path
from . import views

app_name = 'gifConverter'
urlpatterns = [
    path('', views.index, name='index'),    
]