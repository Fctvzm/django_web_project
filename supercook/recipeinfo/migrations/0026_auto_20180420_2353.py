# Generated by Django 2.0.4 on 2018-04-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0025_auto_20180420_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
