from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.forms import ModelForm
from .models import Rezervace
from django import forms

class DateTimeForm(forms.ModelForm):
    class Meta:
        model = Rezervace
        widgets = {
            'Začátek_pronájmu_učebny': DateTimePickerInput(),
            'Konec_pronájmu_učebny': DateTimePickerInput(),
        }
        fields = ['Jakou_učebnu', 'Začátek_pronájmu_učebny', 'Konec_pronájmu_učebny', 'Společnost', 'IČO', 'Email', 'Telefonní_číslo', 'Počet_účastníků', 'Občerstvení', 'Poznámka']
