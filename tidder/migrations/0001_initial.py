# Generated by Django 2.0.5 on 2018-09-14 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=300)),
                ('comment_vote', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('site_url', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('picture', models.ImageField(upload_to='')),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('post_vote', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PostSave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tidder.Post')),
            ],
        ),
        migrations.CreateModel(
            name='UniqueUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signed_up', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tidder.UniqueUser')),
            ],
        ),
        migrations.AddField(
            model_name='postsave',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tidder.UniqueUser'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tidder.UniqueUser'),
        ),
        migrations.AddField(
            model_name='commentpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tidder.Post'),
        ),
        migrations.AddField(
            model_name='commentpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tidder.UniqueUser'),
        ),
        migrations.AddField(
            model_name='admin',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tidder.UserProfile'),
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tidder.UniqueUser'),
        ),
    ]
