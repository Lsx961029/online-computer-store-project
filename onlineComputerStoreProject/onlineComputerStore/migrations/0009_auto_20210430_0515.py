# Generated by Django 2.2.5 on 2021-04-30 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineComputerStore', '0008_auto_20210430_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='topic',
        ),
        migrations.AlterField(
            model_name='discussion',
            name='forum',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='onlineComputerStore.Forum'),
        ),
    ]
