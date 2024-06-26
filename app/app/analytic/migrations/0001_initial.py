# Generated by Django 5.0.4 on 2024-04-13 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'analytic_banks',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('code', models.CharField(max_length=255, unique=True)),
                ('unit', models.CharField(default='тыс.тенге', max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'analytic_reports',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('display', models.IntegerField(blank=True, choices=[(0, 'Decimal'), (1, 'Percent')], null=True)),
                ('order', models.PositiveIntegerField(db_index=True, default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='analytic.indicator')),
            ],
            options={
                'db_table': 'analytic_indicators',
            },
        ),
        migrations.CreateModel(
            name='IndicatorValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytic.bank')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytic.indicator')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytic.report')),
            ],
            options={
                'db_table': 'analytic_indicator_values',
            },
        ),
    ]
