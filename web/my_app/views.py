from django.shortcuts import render
from my_app.models import Product

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def contact_us(request):
    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html', {"products": Product.objects.all()})


