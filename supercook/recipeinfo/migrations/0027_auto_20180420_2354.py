# Generated by Django 2.0.4 on 2018-04-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0026_auto_20180420_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='descriptor',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
