# Generated by Django 3.1.7 on 2021-03-20 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['first_name']},
        ),
    ]
