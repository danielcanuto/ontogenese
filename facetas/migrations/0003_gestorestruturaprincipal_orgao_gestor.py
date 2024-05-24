# Generated by Django 5.0.6 on 2024-05-24 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facetas', '0002_rename_historico_gestaoprincial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GestorEstruturaPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('observacao', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='orgao',
            name='gestor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facetas.gestorestruturaprincipal'),
        ),
    ]