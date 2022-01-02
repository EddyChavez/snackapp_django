from applications.events.models import Event
from django.db import models
from django.conf import settings
from .managers import ProductManager
# Create model product.


class Product(models.Model):
    name = models.CharField('Nombre', max_length=200)
    description = models.CharField('Description', max_length=300)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8, default=0)
    create_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='product_user', on_delete=models.CASCADE)
    image = models.ImageField('Imagen', blank=True,
                              null=True, upload_to='products')
    event = models.ForeignKey(
        Event, related_name='product_event', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.name
