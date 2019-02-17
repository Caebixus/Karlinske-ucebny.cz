from django.shortcuts import render,redirect
from .forms import DateTimeForm

# Create your views here.

def rezervace(request):
    form = DateTimeForm(request.POST or None)
    context = {
        'form': form
        }
    if form.is_valid():
        form.save()
        return redirect('rezervace_poslana')
    else:
        return render(request, 'rezervace.html', context)

def rezervace_poslana(request):
    return render(request, 'rezervace_poslana.html', {})
