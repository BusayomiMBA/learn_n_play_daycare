# Generated by Django 3.1.7 on 2021-04-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210402_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_activity',
            name='time',
            field=models.CharField(default='20:53:14', max_length=9),
        ),
    ]
