# Generated by Django 5.1.2 on 2024-10-21 16:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_publisher_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='games', to=settings.AUTH_USER_MODEL),
        ),
    ]
