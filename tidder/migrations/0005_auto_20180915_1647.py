# Generated by Django 2.0.5 on 2018-09-15 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tidder', '0004_auto_20180915_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniqueuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]