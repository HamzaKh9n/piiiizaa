# Generated by Django 5.0.7 on 2024-11-11 11:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_temp_order_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_order',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
