# Generated by Django 2.0.4 on 2018-04-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0020_auto_20180420_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='descriptor',
            field=models.CharField(default='Assem', max_length=20, unique=True),
        ),
    ]