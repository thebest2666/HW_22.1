# Generated by Django 4.2.2 on 2024-10-19 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0002_product_is_published_product_views_counter_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель",
            ),
        ),
    ]
