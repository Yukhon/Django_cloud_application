# Generated by Django 2.2.12 on 2021-12-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=32, verbose_name='password')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='last updated time')),
            ],
        ),
    ]
