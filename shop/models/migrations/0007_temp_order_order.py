# Generated by Django 5.0.7 on 2024-11-11 11:28

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_pizza_ex_img'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='temp_order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.sellers')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.temp_order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
