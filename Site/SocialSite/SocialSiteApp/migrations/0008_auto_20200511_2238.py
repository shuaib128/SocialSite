# Generated by Django 3.0.2 on 2020-05-12 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialSiteApp', '0007_profile_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(default='Fb/...', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default='00 000 000', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(default='Tw/...', max_length=200),
        ),
    ]