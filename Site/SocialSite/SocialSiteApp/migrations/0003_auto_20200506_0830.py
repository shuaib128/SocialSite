# Generated by Django 3.0.2 on 2020-05-06 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialSiteApp', '0002_profileimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileimage',
            old_name='coverPhoto',
            new_name='images',
        ),
    ]