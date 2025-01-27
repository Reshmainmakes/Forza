# Generated by Django 4.2.13 on 2024-06-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_ordering', '0003_kitchenlunch_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentcleaning',
            name='location',
            field=models.CharField(choices=[('JP23', 'JP23'), ('KP5', 'KP5'), ('TS17', 'TS17')], default='JP23', max_length=50),
        ),
        migrations.AddField(
            model_name='drystoragecleaning',
            name='location',
            field=models.CharField(choices=[('JP23', 'JP23'), ('KP5', 'KP5'), ('TS17', 'TS17')], default='JP23', max_length=50),
        ),
        migrations.AddField(
            model_name='kitchenlate',
            name='location',
            field=models.CharField(choices=[('JP23', 'JP23'), ('KP5', 'KP5'), ('TS17', 'TS17')], default='JP23', max_length=50),
        ),
        migrations.AddField(
            model_name='kitchenlatetask',
            name='location',
            field=models.CharField(choices=[('JP23', 'JP23'), ('KP5', 'KP5'), ('TS17', 'TS17')], default='JP23', max_length=50),
        ),
        migrations.AddField(
            model_name='kitchenlunchtask',
            name='location',
            field=models.CharField(choices=[('JP23', 'JP23'), ('KP5', 'KP5'), ('TS17', 'TS17')], default='JP23', max_length=50),
        ),
        migrations.AddField(
            model_name='kitchenspecialcleaningmonday',
            name='location',
            field=models.CharField(choices=[('JP23', 'JP23'), ('KP5', 'KP5'), ('TS17', 'TS17')], default='JP23', max_length=50),
        ),
        migrations.AddField(
            model_name='terminallate',
            name='location',
            field=models.CharField(choices=[('JP23', 'JP23'), ('KP5', 'KP5'), ('TS17', 'TS17')], default='JP23', max_length=50),
        ),
        migrations.AddField(
            model_name='terminallunch',
            name='location',
            field=models.CharField(choices=[('JP23', 'JP23'), ('KP5', 'KP5'), ('TS17', 'TS17')], default='JP23', max_length=50),
        ),
        migrations.AddField(
            model_name='wednesdaycleaning',
            name='location',
            field=models.CharField(choices=[('JP23', 'JP23'), ('KP5', 'KP5'), ('TS17', 'TS17')], default='JP23', max_length=50),
        ),
    ]
