# Generated by Django 4.2.13 on 2024-06-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produits',
            name='active',
            field=models.BooleanField(null=True),
        ),
    ]
