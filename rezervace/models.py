from django.db import models
from multiselectfield import MultiSelectField
from django.forms import ModelForm

# Create your models here.

TYP_UČEBNY = (
    ('Učebna A', 'Učebna A'),
    ('Učebna B', 'Učebna B'),
    ('Učebna C', 'Učebna C'),
)

TYP_OBČERSTVENÍ = (
    ('Tento základní balíček je účtovaný automaticky - (Káva, voda, čaj, ovocné sirupy)', 'Tento základní balíček je účtovaný automaticky - (Káva, voda, čaj, ovocné sirupy)'),
    ('Slaný', 'Slaný'),
    ('Sladký', 'Sladký'),
    ('Smíšený', 'Smíšený'),
    ('Celodenní balíček', 'Celodenní balíček'),
)

class Rezervace(models.Model):
    Jakou_učebnu = models.CharField(max_length=20, choices=TYP_UČEBNY)
    Začátek_pronájmu_učebny = models.DateTimeField()
    Konec_pronájmu_učebny = models.DateTimeField()
    Email = models.EmailField()
    Společnost = models.CharField(max_length=50, null=True)
    Telefonní_číslo = models.IntegerField()
    Počet_účastníků = models.IntegerField()
    Občerstvení = MultiSelectField(choices=TYP_OBČERSTVENÍ, default='Tento základní balíček je účtovaný automaticky - (Káva, voda, čaj, ovocné sirupy)', blank=True)
    Poznámka = models.TextField(blank=True)
    Objednávka_přijata = models.DateTimeField(auto_now_add=True, blank=True)
    IČO = models.IntegerField()
