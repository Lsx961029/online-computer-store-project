# Generated by Django 2.2.5 on 2021-05-03 05:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('onlineComputerStore', '0006_auto_20210503_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.UUID('bd9815ee-abd1-11eb-bf1c-e23649546827'), editable=False),
        ),
    ]
