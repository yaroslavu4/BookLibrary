# Generated by Django 4.2 on 2024-12-29 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_reader_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='status',
        ),
    ]