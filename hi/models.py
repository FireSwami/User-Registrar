from django.db import models


class Visitors(models.Model):
    first_name = models.CharField(max_length=100, help_text="Ivan", verbose_name="Имя")
    last_name = models.CharField(
        max_length=100, help_text="Ivanov", verbose_name="Фамилия"
    )
    phone_number = models.CharField(max_length=50, blank=True, verbose_name="Телефон")
    time_registration = models.DateTimeField(
        auto_now_add=True, verbose_name="Время регистрации"
    )

    def __str__(self):
        return "{} ({})".format(self.last_name, self.first_name.upper())

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name"], name="unique_together"
            )
        ]
        verbose_name = "Посетитель"
        verbose_name_plural = "Посетители"
        ordering = ["first_name"]
