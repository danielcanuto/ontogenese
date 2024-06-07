# Generated by Django 5.0.6 on 2024-06-07 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facetas', '0013_orgaounidade_atribuicoes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orgaounidade',
            old_name='fim_atividades',
            new_name='fim_termino',
        ),
        migrations.RenameField(
            model_name='orgaounidade',
            old_name='inicio_atividades',
            new_name='inicio_vinculo',
        ),
        migrations.AddField(
            model_name='orgaounidade',
            name='doc_comprovacao',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PeriodoHistoricoParte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacao_da_parte', models.CharField(max_length=250, verbose_name='História da Parte')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('resumo', models.TextField(blank=True, null=True)),
                ('doc_fundamento', models.FileField(blank=True, null=True, upload_to='')),
                ('obs', models.TextField(blank=True, null=True)),
                ('organizacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facetas.orgaounidade', verbose_name='Orgão do Período')),
            ],
            options={
                'verbose_name_plural': 'Faceta da Parte',
            },
        ),
    ]