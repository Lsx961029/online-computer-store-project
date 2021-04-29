# Generated by Django 2.2.5 on 2021-04-29 07:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineComputerStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pwd', models.CharField(max_length=4)),
                ('customer_name', models.CharField(max_length=20)),
                ('card_number', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(6), django.core.validators.MinLengthValidator(6)])),
            ],
        ),
    ]
