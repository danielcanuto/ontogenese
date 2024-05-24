# Generated by Django 5.0.6 on 2024-05-24 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facetas', '0004_paises_gestorestruturaprincipal_nascimento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gestorestruturaprincipal',
            name='nacionalidade',
        ),
        migrations.AddField(
            model_name='paises',
            name='sigla',
            field=models.CharField(default='BR', max_length=2),
        ),
        migrations.AlterField(
            model_name='paises',
            name='nome_do_pais',
            field=models.CharField(default='Brasil', max_length=50),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_estado', models.CharField(max_length=50)),
                ('sigla_estado', models.CharField(max_length=2)),
                ('observacao', models.TextField()),
                ('nacionalidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facetas.paises')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_municipio', models.CharField(max_length=50)),
                ('observacao', models.TextField()),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facetas.estado')),
            ],
        ),
        migrations.AddField(
            model_name='gestorestruturaprincipal',
            name='naturalidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facetas.municipio'),
        ),
    ]
