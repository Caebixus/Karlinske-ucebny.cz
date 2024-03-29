# Generated by Django 2.1.5 on 2019-02-15 10:25

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rezervace', '0003_auto_20190213_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezervace',
            name='IČO',
            field=models.IntegerField(default=123456),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rezervace',
            name='Občerstvení',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Základní balíček v ceně - (Káva, voda, čaj, ovocné sirupy)', 'Základní balíček v ceně - (Káva, voda, čaj, ovocné sirupy)'), ('Slaný', 'Slaný'), ('Sladký', 'Sladký'), ('Smíšený', 'Smíšený'), ('Celodenní balíček', 'Celodenní balíček')], default='Základní balíček v ceně - (Káva, voda, čaj, ovocné sirupy)', max_length=97),
        ),
    ]
