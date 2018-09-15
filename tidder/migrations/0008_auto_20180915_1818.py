# Generated by Django 2.0.5 on 2018-09-15 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tidder', '0007_auto_20180915_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='comments',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tidder.CommentPost'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='posts',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tidder.Post'),
        ),
    ]