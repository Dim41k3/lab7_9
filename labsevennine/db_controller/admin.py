from django.contrib import admin
from django.contrib import admin
from .models import Inventory, OrderItem, OrderData, ProductData

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity_in_stock')
    list_editable = ('quantity_in_stock',)
    list_filter = ('product',)
    search_fields = ('product__prod_name',)
    raw_id_fields = ('product',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'customer', 'order_id')
    search_fields = ('order__customer__username', 'product__prod_name')
    list_editable = ('quantity','price')
    raw_id_fields = ('order', 'product', 'customer')
    readonly_fields = ('order_id', )

@admin.register(OrderData)
class OrderDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_status', 'total_price')
    list_editable = ('total_price',)
    list_filter = ('customer',)
    search_fields = ('customer__username',)
    readonly_fields = ('customer', 'id')
    raw_id_fields = ('customer', )

    

@admin.register(ProductData)
class ProductDataAdmin(admin.ModelAdmin):
    list_display = ('sku', 'prod_name', 'price', 'category')
    list_editable = ('price',)
    search_fields = ('prod_name',)
    list_filter = ('category',)
