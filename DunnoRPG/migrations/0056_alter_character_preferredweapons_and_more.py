# Generated by Django 4.1.7 on 2023-05-10 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DunnoRPG', '0055_alter_effects_bonus_alter_effects_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='preferredWeapons',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='unlikedWeapons',
            field=models.TextField(null=True),
        ),
    ]
