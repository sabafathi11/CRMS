# Generated by Django 5.0 on 2024-01-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=250)),
                ('natural_number', models.CharField(max_length=20)),
                ('salary', models.FloatField(max_length=250)),
            ],
        ),
    ]