# Generated by Django 3.1.7 on 2021-04-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20210404_1916'),
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
            field=models.CharField(default='19:33:18', max_length=9),
        ),
    ]
