from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html', {})


def cenik(request):
    return render(request, 'cenik.html', {})
