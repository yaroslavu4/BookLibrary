# Generated by Django 4.2 on 2024-12-29 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date_available',
            field=models.DateTimeField(null=True),
        ),
    ]