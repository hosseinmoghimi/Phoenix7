# Generated by Django 5.0.6 on 2024-08-31 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_accountingdocumentline_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingdocumentline',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounting.event', verbose_name='event'),
        ),
    ]
