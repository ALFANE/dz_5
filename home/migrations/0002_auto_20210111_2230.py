# Generated by Django 3.1.3 on 2021-01-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
