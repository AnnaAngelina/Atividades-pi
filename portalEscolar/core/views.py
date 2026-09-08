from django.shortcuts import render
from noticias import models

# Create your views here.
def home(request):
    noticias_p = models.Noticia.objects.filter(tags__titulo='Notícia principal')
    noticias = models.Noticia.objects.all()

    return render(request, 'core/home.html', {'noticias': noticias, 'noticias_principais': noticias_p})