from django.urls import path
from . import views

urlpatterns = [
    path('cardapio/', views.menu_view, name='cardapio'),
]
