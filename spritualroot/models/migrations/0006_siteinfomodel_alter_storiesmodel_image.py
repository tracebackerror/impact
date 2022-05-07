# Generated by Django 4.0.4 on 2022-05-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_projectsmodel_storiesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('site_name', models.CharField(help_text='Site Name', max_length=250)),
                ('tag_line', models.CharField(blank=True, help_text='Tag Line', max_length=250, null=True)),
                ('email', models.EmailField(blank=True, help_text='Email', max_length=70, null=True)),
                ('phone', models.CharField(blank=True, help_text='Phone Number', max_length=10, null=True)),
                ('alternate_phone_1', models.CharField(blank=True, help_text='Alternate Phone Numbe 1', max_length=10, null=True)),
                ('alternate_phone_2', models.CharField(blank=True, help_text='Alternate Phone Numbe 2', max_length=10, null=True)),
                ('alternate_phone_3', models.CharField(blank=True, help_text='Alternate Phone Numbe 3', max_length=10, null=True)),
                ('site_address', models.TextField(blank=True, help_text='Site Address', null=True)),
                ('site_logo', models.ImageField(blank=True, help_text='Site Logo', null=True, upload_to='uploads/%Y/%m/%d/')),
                ('site_longitude_lattitude', models.CharField(blank=True, help_text='Maps Location', max_length=250, null=True)),
                ('facebook_page', models.CharField(blank=True, help_text='Facebook Page', max_length=300, null=True)),
                ('instagram_page', models.CharField(blank=True, help_text='Instagram Page', max_length=300, null=True)),
                ('twitter_page', models.CharField(blank=True, help_text='Twitter Page', max_length=300, null=True)),
                ('linkedin_page', models.CharField(blank=True, help_text='LinkedIn Page', max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='storiesmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
