# Generated by Django 4.1.1 on 2023-05-04 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividademodel',
            name='data',
            field=models.DateTimeField(default='2006-10-25', verbose_name='Data'),
        ),
    ]