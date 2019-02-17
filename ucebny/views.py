from django.shortcuts import render

# Create your views here.

def ucebna_A(request):
    return render(request, 'ucebna_A.html', {})

def ucebna_B(request):
    return render(request, 'ucebna_B.html', {})

def ucebna_C(request):
    return render(request, 'ucebna_C.html', {})
