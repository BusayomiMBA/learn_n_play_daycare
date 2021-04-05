# Generated by Django 3.1.7 on 2021-04-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_auto_20210404_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_image',
            field=models.ImageField(blank=True, null=True, upload_to='child/'),
        ),
        migrations.AlterField(
            model_name='daily_activity',
            name='time',
            field=models.CharField(default='20:11:07', max_length=9),
        ),
    ]
