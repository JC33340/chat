# Generated by Django 4.2.6 on 2023-11-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livechats",
            name="category",
            field=models.CharField(max_length=20),
        ),
    ]