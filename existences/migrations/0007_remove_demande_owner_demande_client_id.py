# Generated by Django 5.0.4 on 2024-04-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('existences', '0006_alter_demande_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande',
            name='owner',
        ),
        migrations.AddField(
            model_name='demande',
            name='client_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
