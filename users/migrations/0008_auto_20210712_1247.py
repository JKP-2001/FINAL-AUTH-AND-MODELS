# Generated by Django 3.2.4 on 2021-07-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210712_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='user.first_name', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='roll',
            field=models.CharField(default='user.last_name', max_length=9),
        ),
    ]
