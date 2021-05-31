from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Product, User
# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST)
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

def user_register(request):
    if request.method == 'POST':
        if User.objects.filter(userEmail=request.POST['useremail']).exists():
            return render(request, 'products/register.html', {
                'warning': 'that email exists'
            })
        else:
            user = User(userName=request.POST['username'],
                        userEmail=request.POST['useremail'],
                        userPassword=request.POST['userpassword'])
            user.save()
            user_id = user.id
            return HttpResponseRedirect(reverse('userpage', args=(user_id,)))

    return render(request, 'products/register.html')

def user_login(request):
    if request.method == 'POST':
        if User.objects.filter(userEmail=request.POST['useremail'], userPassword=request.POST['userpassword']).exists():
            user_id = User.objects.get(userEmail=request.POST['useremail']).id
            return HttpResponseRedirect(reverse('userpage', args=(user_id,)))
        else:
            return render(request, 'products/login.html', {
                'message': 'login failed'
            })
    return render(request, 'products/login.html')

def user_page(request, id):
    return render(request, 'products/product.html', {
        'products': Product.objects.all()
    })
