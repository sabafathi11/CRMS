# Generated by Django 4.2.9 on 2024-01-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_alter_payment_dates_paid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='use_insurance',
            name='paid_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='use_insurance',
            name='request_answer',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]