from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from .forms import *

# Create your views here.
def listar_noticias(request):
    noticias = Noticia.objects.all()

    return render(request, 'noticias/listar_noticias.html', {'noticias': noticias})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.all()

    return render(request, 'noticias/listar_categ.html', {'categorias': categorias, 'noticias': noticias})

def detalhes_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)

    return render(request, 'noticias/detalhes_noticia.html', {'noticia': noticia})

def listar_tags(request):
    tags = Tag.objects.all()
    noticias = Noticia.objects.all()

    return render(request, 'noticias/listar_tags.html', {'tags': tags, 'noticias': noticias})

def detalhes_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    noticias = tag.noticias.all()
    
    return render(request, 'noticias/detalhes_tag.html', {'tag': tag, 'noticias': noticias})

def criar_categoria(request):

    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            Categoria.objects.create(nome=nome)

            messages.success(request, "Categoria cadastrada com sucesso!")
            return redirect('listar_categorias')

    else:
        form = CategoriaForm()

    return render(request, 'noticias/criar_categoria.html', {'form': form})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria atualizada com sucesso!")
            return redirect('listar_categorias')
    else:
       form = CategoriaForm(instance=categoria)
    return render(request, 'noticias/editar_categoria.html', {'form': form, 'categoria': categoria})

def excluir_categoria(request, id):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":

        try:
            categoria.delete()
            messages.error(request, "Categoria deletada com sucesso!")
        except ProtectedError:
            messages.error(request, "Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.")

        return redirect("listar_categorias")

    categoria.delete()
    return render(request, 'noticias/listar_categorias.html', {'categorias': categorias})

def adicionar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)

        if form.is_valid():
            form.save()
            noticia = form.save(commit=False)
            noticia.save()
            form.save_m2m()
            messages.success(request, "Notícia cadastrada com sucesso!")
            return redirect('listar_noticias')

    else:
        form = NoticiaForm()

    return render(request, 'noticias/adicionar_noticia.html', {'form': form})

def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)

        if form.is_valid():
            form.save()
            messages.success(request, "Notícia atualizada com sucesso!")
            return redirect('listar_noticias')

    else:
        form = NoticiaForm(instance=noticia)

    return render(request, 'noticias/editar_noticia.html', {'form': form, 'noticia': noticia})

def excluir_noticia(request, id):
    noticias = Noticia.objects.all()
    noticia = get_object_or_404(Noticia, id=id)

    if request.method == "POST":

        noticia.delete()
        messages.success(request, "Notícia deletada com sucesso!")
        return redirect("listar_noticias")

    noticia.delete()
    return render(request, 'noticias/listar_noticias.html', {'noticias': noticias})

def criar_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Tag criada com sucesso!")
            return redirect('listar_tags')

    else:
        form = TagForm()

    return render(request, 'noticias/criar_tag.html', {'form': form})

def editar_tag(request, id):
    tag = get_object_or_404(Tag, id=id)

    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)

        if form.is_valid():
            form.save()
            messages.success(request, "Tag atualizada com sucesso!")
            return redirect('listar_tags')

    else:
        form = TagForm(instance=tag)

    return render(request, 'noticias/editar_tag.html', {'form': form, 'tag': tag})

def excluir_tag(request, id):
    tags = Tag.objects.all()
    tag = get_object_or_404(Tag, id=id)

    if request.method == "POST":

        tag.delete()
        messages.success(request, "Tag deletada com sucesso!")
        return redirect("listar_tags")

    tag.delete()
    return render(request, 'noticias/listar_noticias.html', {'tags': tags, 'tag': tag})