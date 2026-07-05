from django.shortcuts import render
from servicos import views as viewservice
from produtos import views as viewproducts

# Create your views here.
def home(request):
    context = {'servicos': viewservice.returnServico, 'produtos': viewproducts.returnProdutos}
    return render(request, 'core/home.html', context)