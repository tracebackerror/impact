# Generated by Django 4.0.3 on 2022-05-04 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]