# Generated by Django 4.2.2 on 2023-06-20 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flotas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('latidud', models.DecimalField(decimal_places=8, max_digits=12)),
                ('longitud', models.DecimalField(decimal_places=8, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('distancia', models.DecimalField(decimal_places=2, max_digits=12)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='rutas_destino', to='travels.ciudad')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='rutas_origen', to='travels.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llegada', models.DateTimeField(verbose_name='hora de llegada')),
                ('salida', models.DateTimeField(verbose_name='hora de salida')),
                ('flota', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='flotas.flota')),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='travels.ruta')),
            ],
        ),
    ]
