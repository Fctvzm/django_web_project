# Generated by Django 2.0.4 on 2018-04-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0014_auto_20180420_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, choices=[('g', 'gramm'), ('tbsp', 'tablespoon'), ('ml', 'mililiter'), ('l', 'liter'), ('kg', 'kilogramm'), ('', '')], default='', max_length=10, null=True),
        ),
    ]