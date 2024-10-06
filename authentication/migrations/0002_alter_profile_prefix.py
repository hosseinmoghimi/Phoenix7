# Generated by Django 5.0.6 on 2024-10-03 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prefix',
            field=models.CharField(choices=[('آقای', 'آقای'), ('خانم', 'خانم'), ('شرکت', 'شرکت'), ('دکتر', 'دکتر'), ('مهندس', 'مهندس')], default='آقای', max_length=50, verbose_name='پیشوند'),
        ),
    ]
