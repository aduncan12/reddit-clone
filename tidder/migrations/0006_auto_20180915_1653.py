# Generated by Django 2.0.5 on 2018-09-15 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidder', '0005_auto_20180915_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uniqueuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
    ]