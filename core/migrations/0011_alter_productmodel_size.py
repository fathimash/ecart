# Generated by Django 4.1.2 on 2022-11-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_remove_dressmodel_parent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="size",
            field=models.CharField(max_length=10),
        ),
    ]
