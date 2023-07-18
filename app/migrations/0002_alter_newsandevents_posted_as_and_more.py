# Generated by Django 4.2.1 on 2023-05-31 20:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsandevents",
            name="posted_as",
            field=models.CharField(
                choices=[("Новости", "Новости"), ("События", "События")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="semester",
            name="semester",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Первый", "Первый"),
                    ("Второй", "Второй"),
                    ("Третий", "Третий"),
                    ("Четвертый", "Четвертый"),
                ],
                max_length=10,
            ),
        ),
    ]