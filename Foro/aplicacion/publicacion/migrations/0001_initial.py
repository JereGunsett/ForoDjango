# Generated by Django 3.2 on 2023-10-29 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('tema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.user')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tema.tema')),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
    ]
