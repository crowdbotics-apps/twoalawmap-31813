# Generated by Django 2.2.24 on 2021-11-02 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Local_data",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("county", models.TextField()),
                ("state", models.TextField(blank=True, null=True)),
                ("risk", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
