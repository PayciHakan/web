# Generated by Django 4.0.4 on 2022-06-05 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0021_paylasim_yazılımurunumu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paylasim',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.category'),
        ),
        migrations.AlterField(
            model_name='paylasim',
            name='gönderiFoto',
            field=models.ImageField(blank=True, upload_to='Paylasim'),
        ),
    ]
