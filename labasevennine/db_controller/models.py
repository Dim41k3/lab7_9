from django.db import models

class Customer(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()
    address = models.TextField()

    class Meta:
        db_table = 'customer_data'


class Inventory(models.Model):
    product = models.ForeignKey('ProductData', on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()

    class Meta:
        db_table = 'inventory_data'


class OrderItem(models.Model):
    order = models.ForeignKey('OrderData', on_delete=models.CASCADE)
    product = models.ForeignKey('ProductData', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_item'


class OrderData(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_status = models.TextField()
    total_price = models.IntegerField()

    class Meta:
        db_table = 'order_data'


class ProductData(models.Model):
    sku = models.TextField()
    prod_name = models.TextField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.TextField()

    class Meta:
        db_table = 'product_data'
