# Generated by Django 3.1.7 on 2021-03-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerson', '0003_auto_20210320_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/user.png', null=True, upload_to='static/images'),
        ),
    ]
