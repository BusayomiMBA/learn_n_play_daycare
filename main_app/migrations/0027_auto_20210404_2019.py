# Generated by Django 3.1.7 on 2021-04-04 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_auto_20210404_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='daily_activity',
            name='time',
            field=models.CharField(default='20:19:22', max_length=9),
        ),
    ]