# Generated by Django 4.2 on 2023-05-25 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zahrweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Details',
            field=models.TextField(help_text='News details', max_length=30000),
        ),
    ]
