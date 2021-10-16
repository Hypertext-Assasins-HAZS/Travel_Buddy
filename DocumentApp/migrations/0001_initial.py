# Generated by Django 3.2.6 on 2021-10-15 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docType', models.CharField(max_length=45, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('expDate', models.DateField(default=django.utils.timezone.now)),
                ('docImg', models.ImageField(default='docImg_default.png', upload_to='documents')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
