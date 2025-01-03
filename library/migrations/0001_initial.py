# Generated by Django 4.2 on 2024-12-29 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Book name')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date added')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registration date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_taken', models.DateTimeField(auto_now_add=True, verbose_name='Date taken')),
                ('date_due', models.DateTimeField(verbose_name='Date to be returned')),
                ('date_returned', models.DateTimeField(blank=True, null=True, verbose_name='Date Returned')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='library.book', verbose_name='Book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='library.reader', verbose_name='Reader')),
            ],
        ),
    ]
