# Generated by Django 4.0.4 on 2022-05-14 18:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_alter_contactmodel_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Title', max_length=250)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(help_text='Location', max_length=50)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Description', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]