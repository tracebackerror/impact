# Generated by Django 4.0.4 on 2022-05-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_alter_volunteermodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteermodel',
            name='image',
            field=models.ImageField(blank=True, help_text='resolution of 256x258', null=True, upload_to='volunteers_image'),
        ),
    ]
