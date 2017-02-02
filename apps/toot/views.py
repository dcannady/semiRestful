from django.shortcuts import render, redirect
from .models import Products
from django.core.urlresolvers import reverse

def index(request):
    context= {
    'product': Products.objects.all()
    }
    return render(request, 'toot/index.html', context)

def new(request):
    return render(request, 'toot/new.html')

def create(request):
    Products.objects.create(name=request.POST['name'], description=request.POST['description'],price=request.POST['price'])
    return redirect(reverse('products_index'))

def show(request, product_id):
    context= {
        'product': Products.objects.filter(id=product_id)
    }
    return render(request, 'products/show.html', context)

def edit(request, product_id):
    context={
        'product': Products.object.filter(id=product_id)
    }
    return render(request, 'products/edit.html', context)

def update(request, product_id):
    Products.objects.update(product_id, request.POST)
    return redirect(reverse('products_index'))

def destroy(request, product_id):
    Products.objects.filter(id=product_id).delete()
    return redirect(reverse('products_index'))
# Create your views here.
