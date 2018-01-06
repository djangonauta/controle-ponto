# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-06 11:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CargaHorária',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ano', models.IntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DiaTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('dia', models.IntegerField()),
                ('entrada_manhã', models.TimeField(default=datetime.time(0, 0))),
                ('saída_manhã', models.TimeField(default=datetime.time(0, 0))),
                ('entrada_tarde', models.TimeField(default=datetime.time(0, 0))),
                ('saída_tarde', models.TimeField(default=datetime.time(0, 0))),
                ('observação', models.TextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MêsTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('referência', models.CharField(choices=[('01', 'janeiro'), ('02', 'fevereiro'), ('03', 'março'), ('04', 'abril'), ('05', 'maio'), ('06', 'junho'), ('07', 'julho'), ('08', 'agosto'), ('09', 'setembro'), ('10', 'outubro'), ('11', 'novembro'), ('12', 'dezembro')], default='01', max_length=2)),
                ('carga_horária', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meses', to='ponto.CargaHorária')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('siape', models.CharField(max_length=16)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pontos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='diatrabalho',
            name='mês',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dias', to='ponto.MêsTrabalho'),
        ),
        migrations.AddField(
            model_name='cargahorária',
            name='ponto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carga_horária', to='ponto.Ponto'),
        ),
    ]