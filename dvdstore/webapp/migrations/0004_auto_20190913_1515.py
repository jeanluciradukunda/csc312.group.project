# Generated by Django 2.2.4 on 2019-09-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190913_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='TransactionNumber',
            field=models.CharField(max_length=250),
        ),
    ]
