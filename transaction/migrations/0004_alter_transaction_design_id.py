# Generated by Django 4.0.1 on 2022-04-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_transaction_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='design_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='design_id'),
        ),
    ]