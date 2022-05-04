# Generated by Django 4.0.3 on 2022-05-04 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_contactform_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='date',
            new_name='modified_date',
        ),
        migrations.AddField(
            model_name='contactform',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]