# Generated by Django 2.0.4 on 2018-04-19 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0017_auto_20180420_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoplist',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
