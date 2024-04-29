from django.db import models


def product_image_path(instance, filename):
    return f'product/images/{instance.name}/{filename}'


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to=product_image_path)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'product'

    def __str__(self):
        return f'Товар {self.title}'
