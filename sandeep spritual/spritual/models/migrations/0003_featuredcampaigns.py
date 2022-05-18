# Generated by Django 4.0.4 on 2022-05-17 11:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_alter_projectsmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedCampaigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('feature_hashlink', models.CharField(help_text='Hashlink of featured campaign e.g. Life, Food, Education etc.', max_length=50)),
                ('feature_heading', models.CharField(help_text='Heading of featured campaign', max_length=100)),
                ('feature_description', ckeditor.fields.RichTextField()),
                ('feature_donation_goal', models.PositiveIntegerField(default=1)),
                ('feature_donation_raised', models.PositiveIntegerField(default=1)),
                ('feature_donation_to_go', models.PositiveIntegerField(default=1)),
                ('feature_bar_data', models.PositiveIntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='featured_campaign_image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
