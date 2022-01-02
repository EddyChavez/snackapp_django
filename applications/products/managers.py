from django.db import models

class ProductManager(models.Manager):

    def product_event(self, idEvent):
        return self.filter(
            event=idEvent,
        ).order_by('id')
