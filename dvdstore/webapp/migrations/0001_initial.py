# Generated by Django 2.2.4 on 2019-09-10 17:37

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
            name='DVD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('InStock', models.BooleanField(default=True)),
                ('Synopsis', models.TextField()),
                ('BookingPickup', models.CharField(max_length=255)),
                ('NumOfTimesRented', models.IntegerField(default=0)),
                ('ImageDVD', models.ImageField(upload_to='pics')),
                ('PriceDVD', models.IntegerField(default=0)),
                ('NumDaysBooked', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionNumber', models.IntegerField()),
                ('RentDate', models.CharField(max_length=250)),
                ('DueDate', models.CharField(max_length=255)),
                ('MovieTitle', models.CharField(max_length=255)),
                ('Payment_Method', models.CharField(max_length=255)),
                ('users_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fraud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FraudID', models.IntegerField()),
                ('FraudScore', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
