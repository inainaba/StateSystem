from django.urls import path

from . import views

app_name = 'stateapp'

urlpatterns = [
    path('index/', views.index, name='index'),
]
