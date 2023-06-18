# Generated by Django 4.2.2 on 2023-06-18 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del campeonato')),
                ('nombreausp', models.CharField(max_length=50, verbose_name='Nombre del auspiciante')),
            ],
        ),
        migrations.CreateModel(
            name='Campeonato_equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbolec.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Equipof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre del equipo')),
                ('siglas', models.CharField(max_length=30)),
                ('tusername', models.CharField(max_length=30, verbose_name='Usuario de Twitter')),
                ('campeonatos', models.ManyToManyField(through='futbolec.Campeonato_equipo', to='futbolec.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre Jugador')),
                ('posicion', models.CharField(max_length=50)),
                ('camiseta', models.ImageField(upload_to='', verbose_name='Numero de camiseta')),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='futbolec.equipof')),
            ],
        ),
        migrations.AddField(
            model_name='campeonato_equipo',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbolec.equipof'),
        ),
        migrations.AddField(
            model_name='campeonato',
            name='equipos',
            field=models.ManyToManyField(through='futbolec.Campeonato_equipo', to='futbolec.equipof'),
        ),
    ]