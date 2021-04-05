# Generated by Django 3.1.7 on 2021-04-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_auto_20210404_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_activity',
            name='activity',
            field=models.CharField(choices=[('W', 'Welcome'), ('B', 'BreakFast'), ('L', 'Library'), ('W', 'Writing'), ('M', 'Music'), ('R', 'Reading'), ('S', 'Spelling'), ('F', 'Lunch'), ('C', 'ComputerLab'), ('G', 'Gym'), ('W', 'Math'), ('N', 'Snacks'), ('A', 'ReadingAloud'), ('D', 'Dancing')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='daily_activity',
            name='time',
            field=models.CharField(default='02:05:58', max_length=9),
        ),
    ]