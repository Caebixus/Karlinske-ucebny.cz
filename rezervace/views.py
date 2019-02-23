from django.shortcuts import render,redirect
from .forms import DateTimeForm
from django.core.mail import send_mail
from .models import Rezervace
# Create your views here.

def rezervace(request):
    form = DateTimeForm(request.POST or None)
    context = {
        'form': form
        }
    if form.is_valid():
        form.save()

        data = form.cleaned_data
        ucebna = data['Jakou_učebnu']
        datumA = data['Začátek_pronájmu_učebny']
        datumB = data['Konec_pronájmu_učebny']
        ico = data['IČO']
        email = data['Email']
        phone = data['Telefonní_číslo']
        pocet = data['Počet_účastníků']
        obcerstveni = data['Občerstvení']
        poznamka = data['Poznámka']

        send_mail(
            'Nová poptávka na pronájem učebny',
            'Dobrý den, přišla nová poptávka na pronájem učebny: ' +
            '\nEmail: ' + str(email) +
            '\nJaká učebna: ' + str(ucebna) +
            '\nDatum začátku: ' + str(datumA) +
            '\nDatum konce: ' + str(datumB) +
            '\nIČO: ' + str(ico) +
            '\nTelefon: ' + str(phone) +
            '\nPočet účastníků: ' + str(pocet) +
            '\nObčerstvení zaškrtnuto: ' + str(obcerstveni) +
            '\nPoznámka: ' + str(poznamka) +
            '\npřípadně se přihlašte na karlinske-ucebny.cz/admin',
            'info.zadavatel@gmail.com',
            ['ma.davidlangr@gmail.com'],
            fail_silently=False,
            )

        return redirect('rezervace_poslana')
    else:
        return render(request, 'rezervace.html', context)

def rezervace_poslana(request):
    return render(request, 'rezervace_poslana.html', {})
