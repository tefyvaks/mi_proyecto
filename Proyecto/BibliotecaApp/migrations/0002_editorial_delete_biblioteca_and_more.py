# Generated by Django 4.2.5 on 2023-09-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BibliotecaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('listaLibros', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Biblioteca',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='librosPrestados',
        ),
    ]
