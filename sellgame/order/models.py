from django.db import models

from catalog.models import Product


class Order(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Время последнего изменения")
    paid = models.BooleanField(default=False, verbose_name="Оплачен?")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items', verbose_name="Номер заказа")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items', verbose_name="Игры")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


