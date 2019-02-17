from django.contrib import admin

# Register your models here.
from .models import Rezervace

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'Objednávka_přijata', 'Jakou_učebnu', 'Začátek_pronájmu_učebny', 'Konec_pronájmu_učebny','Email', 'Telefonní_číslo',)
    list_filter = ('Jakou_učebnu', 'Objednávka_přijata',)
    search_fields = ('Email',)

admin.site.register(Rezervace, PostAdmin)
