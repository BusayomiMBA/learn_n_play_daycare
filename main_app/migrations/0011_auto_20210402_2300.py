# Generated by Django 3.1.7 on 2021-04-02 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20210402_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_activity',
            name='time',
            field=models.CharField(default='23:00:48', max_length=9),
        ),
    ]
