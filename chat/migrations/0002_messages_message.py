# Generated by Django 4.2.6 on 2023-11-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="messages",
            name="message",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
