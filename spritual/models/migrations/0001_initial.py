# Generated by Django 4.0.4 on 2022-05-09 12:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=50)),
                ('last_name', models.CharField(help_text='Last Name', max_length=50)),
                ('email', models.EmailField(blank=True, help_text='Email', max_length=70, null=True)),
                ('phone', models.CharField(help_text='Phone Number', max_length=10)),
                ('comments', models.CharField(blank=True, help_text='Phone Number', max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GetHelpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(help_text='First Name', max_length=50)),
                ('last_name', models.CharField(help_text='Last Name', max_length=50)),
                ('email', models.EmailField(blank=True, help_text='Email', max_length=70, null=True)),
                ('phone', models.CharField(help_text='Phone Number', max_length=10)),
                ('get_help_for', models.CharField(choices=[('RHC', 'Rehabilitation'), ('DDA', 'Drug De Addiction'), ('SDDA', 'Smoking De Addiction'), ('ADA', 'Alcohol De-Addiction'), ('MC', 'Mental Counselling'), ('OLH', 'Old Aged Home'), ('CS', 'Childcare Support'), ('OTH', 'Others')], default='RHC', max_length=100)),
                ('address', models.TextField(blank=True, help_text='Address', null=True)),
                ('country', models.CharField(choices=[('IN', 'India'), ('OTH', 'Others')], default='IN', max_length=50)),
                ('state', models.CharField(choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('CT', 'Chhattisgarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PY', 'Puducherry'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UT', 'Uttarakhand'), ('WB', 'West Bengal'), ('OTH', 'Others')], default='MH', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
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
        migrations.CreateModel(
            name='VolunteerMoodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(help_text='First Name', max_length=50)),
                ('last_name', models.CharField(help_text='Last Name', max_length=50)),
                ('email', models.EmailField(blank=True, help_text='Email', max_length=70, null=True)),
                ('phone', models.CharField(help_text='Phone Number', max_length=10)),
                ('volunteering_for', models.CharField(choices=[('BLC', 'Blood Donation Camp'), ('RHC', 'Rehabilation Camp'), ('CRC', 'Child Related Camp'), ('OTH', 'Others Activities'), ('ALL', 'ALL')], default='ALL', max_length=100)),
                ('address', models.TextField(blank=True, help_text='Address', null=True)),
                ('country', models.CharField(choices=[('IN', 'India'), ('OTH', 'Others')], default='IN', max_length=50)),
                ('state', models.CharField(choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('CT', 'Chhattisgarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PY', 'Puducherry'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UT', 'Uttarakhand'), ('WB', 'West Bengal'), ('OTH', 'Others')], default='MH', max_length=50)),
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
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
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