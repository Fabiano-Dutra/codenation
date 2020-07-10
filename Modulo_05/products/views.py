from django.shortcuts import render, redirect
from products.models import Product
from products.forms import ProductModelForm


# Toda função da view recebe uma request
def list_products(request):
    # Fazendo a leitura de todos os produtos
    products = Product.objects.all()

    # contexto sempre é um dicionário
    context = {
        'products': products
    }

    # Agora vamos retornar uma mensagem com o render
    return render(request, 'products/list.html', context=context)

def create_product(request):
    if request.method == 'POST':
        #salvar form, trazendo formulário para criação de produto
        form = ProductModelForm(request.POST)
        if form.is_valid():
            #True -> é valido
            form.save()
            form = ProductModelForm()
    else:
        # Get form
        form = ProductModelForm()

    context = {
        'form': form
    }
    return render(request, 'products/create.html', context=context)


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('products:list')


def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        #salvar form, trazendo dados instaciados em product para o formulário da  tela.
        form = ProductModelForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        # GET
        # Trazendo dados instanciados em product para o formulário.
        form = ProductModelForm(instance=product)

    context = {
        'form': form,
    }

    return render(request, 'products/update.html', context=context)

