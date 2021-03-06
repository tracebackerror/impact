# Generated by Django 4.0.4 on 2022-05-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_featuredcampaigns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredcampaigns',
            name='feature_bar_data',
            field=models.PositiveIntegerField(default=1, help_text='Maximum bar size 100'),
        ),
        migrations.AlterField(
            model_name='featuredcampaigns',
            name='feature_description',
            field=models.CharField(help_text='Description of featured campaign', max_length=100),
        ),
        migrations.AlterField(
            model_name='featuredcampaigns',
            name='image',
            field=models.ImageField(help_text='400x225 resolution', upload_to='featured_campaign_image'),
        ),
    ]
