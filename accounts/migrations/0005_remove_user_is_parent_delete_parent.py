# Generated by Django 4.2.1 on 2023-06-02 12:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_user_patronymic"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_parent",
        ),
        migrations.DeleteModel(
            name="Parent",
        ),
    ]
