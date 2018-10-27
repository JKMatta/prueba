# Generated by Django 2.0.6 on 2018-10-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptarRescatado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('celular', models.IntegerField(max_length=9)),
                ('region', models.CharField(max_length=25)),
                ('comuna', models.CharField(max_length=25)),
                ('tipo_casa', models.CharField(max_length=25)),
                ('nombre_rescatado', models.CharField(max_length=25)),
                ('correo', models.CharField(max_length=50)),
                ('adop_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
