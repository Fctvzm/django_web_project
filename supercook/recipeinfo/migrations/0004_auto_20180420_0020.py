# Generated by Django 2.0.4 on 2018-04-19 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0003_auto_20180420_0011'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shoplist',
            unique_together={('recipe', 'ingredient')},
        ),
    ]
