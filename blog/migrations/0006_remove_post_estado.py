# Generated by Django 2.0.6 on 2018-10-27 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181026_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Estado',
        ),
    ]
