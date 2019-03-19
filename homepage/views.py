from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html', {})

def sitemap(request):
    return render(request, 'sitemap.xml', {})

def cenik(request):
    return render(request, 'cenik.html', {})
