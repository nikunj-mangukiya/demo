# Generated by Django 4.2.4 on 2023-08-12 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0002_alter_invoiceitem_invoice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoiceitem",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="invoice.invoice",
            ),
        ),
    ]