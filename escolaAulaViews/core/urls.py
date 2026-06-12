from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('listalunos/', views.listEstudantes, name='listestudantes'),
    path('sobrenos/', views.sobreNos, name='sobrenos')
]