from django.db import models
from users.models import User

class Inventory(models.Model):
    product = models.ForeignKey('ProductData', on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.product.prod_name

    class Meta:
        db_table = 'inventory_data'


class OrderItem(models.Model):
    order = models.ForeignKey('OrderData', on_delete=models.CASCADE)
    product = models.ForeignKey('ProductData', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.prod_name

    class Meta:
        db_table = 'order_item'


class OrderData(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.TextField()
    total_price = models.IntegerField()

    def __str__(self):
        return f"Order #{self.pk}"

    class Meta:
        db_table = 'order_data'


class ProductData(models.Model):
    sku = models.TextField()
    prod_name = models.TextField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.TextField()

    def __str__(self):
        return self.prod_name

    class Meta:
        db_table = 'product_data'
