# Generated by Django 4.0.4 on 2022-05-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_remove_ariza_gelenfoto_alter_paylasim_gönderifoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
    ]
