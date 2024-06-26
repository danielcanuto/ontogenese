# Generated by Django 5.0.6 on 2024-06-07 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facetas', '0015_niveladmin_alter_tipoadminstracao_options_setor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodohistorico',
            options={'verbose_name_plural': '01 - Faceta História do Todo'},
        ),
        migrations.AlterModelOptions(
            name='periodohistoricoparte',
            options={'verbose_name_plural': '02 - Faceta História da Parte'},
        ),
        migrations.AlterModelOptions(
            name='setor',
            options={'verbose_name_plural': '03 - Faceta Organico Estrutural'},
        ),
        migrations.AlterField(
            model_name='orgaounidade',
            name='doc_comprovacao',
            field=models.FileField(blank=True, null=True, upload_to='fundamentacao/'),
        ),
        migrations.AlterField(
            model_name='periodohistorico',
            name='doc_fundamento',
            field=models.FileField(blank=True, null=True, upload_to='fundamentacao/'),
        ),
        migrations.AlterField(
            model_name='periodohistoricoparte',
            name='doc_fundamento',
            field=models.FileField(blank=True, null=True, upload_to='fundamentacao/'),
        ),
        migrations.AlterField(
            model_name='setor',
            name='doc_comprovacao',
            field=models.FileField(blank=True, null=True, upload_to='fundamentacao/'),
        ),
        migrations.CreateModel(
            name='ConfiguracaoFuncional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacao', models.CharField(max_length=250)),
                ('arae_atuacao', models.CharField(choices=[('fim', 'FIM'), ('meio', 'MEIO')], max_length=10)),
                ('configuracao_funcional', models.CharField(choices=[('função', 'FUNÇÃO'), ('sub Função', 'SUB FUNÇÂO'), ('atividade', 'ATIVIDADE')], max_length=10)),
                ('existencia', models.CharField(choices=[('fato', 'De Fato'), ('direito', 'De Direito')], max_length=10)),
                ('doc_comprovacao', models.FileField(blank=True, null=True, upload_to='fundamentacao/')),
                ('atribuicao', models.TextField()),
                ('obs', models.TextField()),
                ('unidade_administrativa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facetas.setor', verbose_name='Unidade Administrativa')),
            ],
        ),
    ]
