from django.db import models

from user.models import User


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'order'

    def __str__(self):
        return f'Заказ от {self.owner.username}'
