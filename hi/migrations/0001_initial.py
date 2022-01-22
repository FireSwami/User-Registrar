# Generated by Django 4.0.1 on 2022-01-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Visitors",
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
                (
                    "first_name",
                    models.CharField(
                        help_text="Ivan", max_length=100, verbose_name="Имя"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Ivanov", max_length=100, verbose_name="Фамилия"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=50, verbose_name="Телефон"),
                ),
                (
                    "time_registration",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время регистрации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Посетитель",
                "verbose_name_plural": "Посетители",
                "ordering": ["first_name"],
            },
        ),
        migrations.AddConstraint(
            model_name="visitors",
            constraint=models.UniqueConstraint(
                fields=("first_name", "last_name"), name="unique_together"
            ),
        ),
    ]
