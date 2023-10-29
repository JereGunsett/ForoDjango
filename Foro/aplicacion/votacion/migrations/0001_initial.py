# Generated by Django 3.2 on 2023-10-29 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voto', models.IntegerField(choices=[(1, 'Me gusta'), (-1, 'No me gusta')])),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacion.publicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.user')),
            ],
            options={
                'verbose_name': 'Votacion',
                'verbose_name_plural': 'Votaciones',
            },
        ),
    ]
