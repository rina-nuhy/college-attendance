# Generated by Django 3.2.10 on 2021-12-11 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
    ]
