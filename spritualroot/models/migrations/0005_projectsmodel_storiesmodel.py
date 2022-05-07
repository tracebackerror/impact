# Generated by Django 4.0.4 on 2022-05-07 17:10

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_gethelpmodel_volunteermoodel_remove_contactform_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Project Title', max_length=250)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/')),
                ('short_url', models.SlugField(max_length=250, unique_for_date='publish')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('meta_keywords', models.CharField(blank=True, help_text='Meta Keywords', max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Project Title', max_length=250)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/')),
                ('short_url', models.SlugField(max_length=250, unique_for_date='publish')),
                ('yt_url', models.CharField(blank=True, help_text='Youtube Video Link', max_length=300, null=True)),
                ('fb_url', models.CharField(blank=True, help_text='Facebook Link Page', max_length=300, null=True)),
                ('ig_url', models.CharField(blank=True, help_text='Instagram Link Page', max_length=300, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('meta_keywords', models.CharField(blank=True, help_text='Meta Keywords', max_length=250, null=True)),
                ('linked_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.projectsmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]