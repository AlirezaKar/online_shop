from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *


def index(request):
    products = Product.objects.all()
    product_feature = ProductFeature.objects.all()
    context = {'products':products}
    return render(request=request, template_name='shop/index.html', context=context)

def checkout(request):
    pass

def shopping_basket_view(request):
    return render(request=request, template_name='shop/shopping_list.html')

def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    context = {'product':product}
    return render(request=request, template_name='shop/product_detail.html', context=context)

@login_required
def add_to_list(request, id):
    product = get_object_or_404(Product, id=id)
    print(request.user.product_count)
    request.user.product_count += 1
    request.user.save()
    print(request.user.product_count)
    messages.success(request, f"Product count updated! You now have {request.user.product_count} products.")
    return redirect(product_detail_view, id=id)