# Generated by Django 2.2.5 on 2021-05-03 19:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('onlineComputerStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.UUID('c657e2ab-ac41-11eb-873f-207918e81943'), editable=False),
        ),
    ]
