# Generated by Django 5.1.6 on 2025-02-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                ("shipping_address", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("completed", "Completed"),
                            ("shipped", "Shipped"),
                        ],
                        max_length=50,
                    ),
                ),
                ("products", models.ManyToManyField(to="products.product")),
            ],
        ),
    ]
