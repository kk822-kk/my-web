from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def contact_us(request):
    return render(request, 'contact.html')

def news(request):
    return render(request, 'news.html')

def photos(request):
    return render(request, 'photos.html')