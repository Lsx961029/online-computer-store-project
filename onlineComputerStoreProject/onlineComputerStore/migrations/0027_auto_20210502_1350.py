# Generated by Django 2.2.5 on 2021-05-02 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineComputerStore', '0026_auto_20210502_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverycompany',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Forum'),
        ),
    ]
