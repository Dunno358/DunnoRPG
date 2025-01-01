# Generated by Django 4.2.1 on 2024-12-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DunnoRPG', '0084_character_hidden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('armor_weight', models.CharField(blank=True, max_length=50)),
                ('skills', models.CharField(blank=True, max_length=255)),
                ('positives', models.TextField(blank=True)),
                ('negatives', models.TextField(blank=True)),
                ('desc', models.TextField(blank=True)),
                ('effects', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]