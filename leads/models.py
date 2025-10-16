from django.db import models
from advertisements.models import Advertisement


class Lead(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Ф. И. О.")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, verbose_name="Рекламная кампания")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"
