# Generated by Django 3.2.6 on 2021-10-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignupApp', '0005_alter_tmsuser_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmsuser',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
