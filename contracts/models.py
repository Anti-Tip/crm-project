from django.db import models
from products.models import Product


class Contract(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Предоставляемая услуга")
    document = models.FileField(upload_to='contracts/', verbose_name="Файл с документом")
    conclusion_date = models.DateField(verbose_name="Дата заключения")
    validity_period = models.CharField(max_length=255, verbose_name="Период действия")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
