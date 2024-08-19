# Generated by Django 5.0.6 on 2024-08-17 01:14

import django.db.models.deletion
import utility.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.account', verbose_name='account')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
            bases=(models.Model, utility.models.LinkHelper),
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='category')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('value', models.CharField(max_length=200, verbose_name='value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.material', verbose_name='product')),
            ],
            options={
                'verbose_name': 'ProductSpecification',
                'verbose_name_plural': 'ProductSpecifications',
            },
            bases=(models.Model, utility.models.LinkHelper),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.account', verbose_name='account')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
            bases=(models.Model, utility.models.LinkHelper),
        ),
    ]
