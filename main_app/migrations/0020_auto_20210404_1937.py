# Generated by Django 3.1.7 on 2021-04-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20210404_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_image',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to='child/'),
        ),
        migrations.AlterField(
            model_name='daily_activity',
            name='time',
            field=models.CharField(default='19:37:47', max_length=9),
        ),
    ]
