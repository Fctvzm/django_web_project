# Generated by Django 2.0.4 on 2018-04-21 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0034_auto_20180421_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
