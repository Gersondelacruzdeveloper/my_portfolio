# Generated by Django 3.1.7 on 2021-03-20 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images/uploads/'),
        ),
    ]
