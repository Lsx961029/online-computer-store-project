# Generated by Django 2.2.5 on 2021-05-01 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineComputerStore', '0027_auto_20210501_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Forum'),
        ),
    ]
