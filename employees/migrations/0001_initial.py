# Generated by Django 4.2 on 2024-11-20 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('seen_code', models.CharField(max_length=10)),
                ('org_code', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=11)),
                ('contract_start', models.DateField(verbose_name='تاریخ شروع قرارداد')),
                ('contract_end', models.DateField(verbose_name='تاریخ اتمام قرارداد')),
                ('contract_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.contracttype')),
            ],
        ),
    ]