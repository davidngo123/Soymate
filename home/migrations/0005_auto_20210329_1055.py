# Generated by Django 3.1.7 on 2021-03-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210326_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ingredients',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='post',
            name='instructions',
            field=models.TextField(max_length=1500),
        ),
    ]
