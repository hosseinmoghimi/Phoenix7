# Generated by Django 5.0.6 on 2024-08-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('processmanagement', '0002_process_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process',
            name='group',
        ),
        migrations.AddField(
            model_name='process',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.group', verbose_name='groups'),
        ),
    ]
