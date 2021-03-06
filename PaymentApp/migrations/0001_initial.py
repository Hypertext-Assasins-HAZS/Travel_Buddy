# Generated by Django 3.2.6 on 2021-10-23 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SignupApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMSPayment',
            fields=[
                ('payment_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField(default=None, null=True)),
                ('mode', models.CharField(default=None, max_length=25, null=True)),
                ('tmsuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SignupApp.tmsuser')),
            ],
        ),
    ]
