# Generated by Django 4.2.4 on 2023-08-12 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoiceitem",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invoice",
                to="invoice.invoice",
            ),
        ),
    ]
