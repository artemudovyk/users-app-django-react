# Generated by Django 4.0 on 2021-12-17 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='group',
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(to='users.UserGroup'),
        ),
    ]
