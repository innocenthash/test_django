# Generated by Django 4.2.13 on 2024-07-01 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='media')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.cour')),
            ],
        ),
    ]
