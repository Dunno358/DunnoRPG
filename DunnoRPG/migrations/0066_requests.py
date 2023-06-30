# Generated by Django 4.2.1 on 2023-06-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DunnoRPG', '0065_items_skilleffects_items_skillstats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=150)),
                ('character', models.CharField(blank=True, max_length=150, null=True)),
                ('model', models.CharField(max_length=150)),
                ('filter_id', models.IntegerField()),
                ('field', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(max_length=150)),
            ],
        ),
    ]
