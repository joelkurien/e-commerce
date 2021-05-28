from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Product
# Create your views here.
def index(request):
    return HttpResponse("hello")

def product_page(request):
    return render(request, 'products/product.html', {
        'products': Product.objects.all()
    })

def product_add(request):
    if request.method == 'POST':
        if len(Product.objects.filter(productName=request.POST['productName'], companyName=request.POST['companyName'])) == 1:
            return HttpResponse('that product exists')
        else:
            product = Product(productName=request.POST['productName'],
                              companyName=request.POST['companyName'],
                              imageUrl=request.POST['imageUrl'],
                              description=request.POST['description'])
            product.save()
            return HttpResponseRedirect(reverse('product'))

    return render(request, 'products/addproduct.html')
