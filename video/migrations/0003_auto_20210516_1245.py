# Generated by Django 3.0.5 on 2021-05-16 12:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20210516_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videounit',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
