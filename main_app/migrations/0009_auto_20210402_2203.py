# Generated by Django 3.1.7 on 2021-04-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210402_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='image',
            new_name='child_image',
        ),
        migrations.AlterField(
            model_name='daily_activity',
            name='time',
            field=models.CharField(default='22:03:28', max_length=9),
        ),
    ]
