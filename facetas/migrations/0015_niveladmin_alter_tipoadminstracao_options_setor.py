# Generated by Django 5.0.6 on 2024-06-07 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facetas', '0014_rename_fim_atividades_orgaounidade_fim_termino_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NivelAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_administrativo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='tipoadminstracao',
            options={'verbose_name_plural': 'Tipos de Administração'},
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_setor', models.CharField(max_length=150)),
                ('sigla', models.CharField(max_length=50)),
                ('existencia_setor', models.CharField(choices=[('fato', 'De Fato'), ('direito', 'De Direito')], max_length=10)),
                ('doc_comprovacao', models.FileField(blank=True, null=True, upload_to='')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('atribuicao', models.TextField()),
                ('obs', models.TextField()),
                ('historico_parte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facetas.periodohistoricoparte', verbose_name='Historico da Parte')),
                ('nivel_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facetas.niveladmin', verbose_name='Nivel Administrativo')),
                ('unidade_superior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facetas.setor', verbose_name='Órgão antecessor')),
            ],
        ),
    ]
