# Generated by Django 5.1.7 on 2025-04-11 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='till_when_date',
            field=models.DateField(verbose_name='till_when'),
        ),
    ]
