from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from db_controller.models import ProductData, Inventory, OrderItem, OrderData
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@login_required
def ordering(request):
    if request.method == 'POST':
        try:
            sku = request.POST.get('sku')
            product = ProductData.objects.get(sku=sku)
            order_item = OrderItem(quantity=1, price=product.price, product_id=product.id, 
                                    customer_id=request.user.id, order_id=None)
            order_item.save()
            print(order_item)
            return render(request, 'shop.html')
        except Exception as e:
            print("ordering", e)
            return HttpResponse("Error processing your request.")
    else:
        return HttpResponse("Error processing your request.")

def info(request):
    if request.method == 'POST':
        try:
            sku = request.POST.get('sku')
            for item in ProductData.objects.filter(sku=sku):
                prod_name = item.prod_name
                price = item.price
                category = item.category
                description = item.description
            context = {"d_prod":{"prod_name":prod_name, "category":category,"description":description,
                                 "sku":sku, "price":price}}
            return render(request, 'info.html', context)
        except Exception as e:
            print("ordering", e)
            return HttpResponse("Error processing your request.")
    else:
        return HttpResponse("Error processing your request.")

def sensors(request):
    products = ProductData.objects.filter(category="Sensor")
    prod_dict = {}
    for product in products:
        qr_obj = Inventory.objects.filter(product=product.id)
        for object in qr_obj:
            quantity_in_stock = object.quantity_in_stock
        prod_dict[product.sku] = {
            "prod_name": product.prod_name,
            "price": product.price,
            "quantity": quantity_in_stock
        }
    
    if 'sort_by_price' in request.POST:
        sorted_by_price = dict(sorted(prod_dict.items(), key=lambda x: x[1]["price"]))
        return render(request, 'sensors.html', {"products": sorted_by_price})
    
    if 'sort_by_name' in request.POST:
        sorted_by_name = dict(sorted(prod_dict.items(), key=lambda x: x[1]["prod_name"]))
        return render(request, 'sensors.html', {"products": sorted_by_name})
    
    return render(request, 'sensors.html', {"products": prod_dict})

def cameras(request):
    products = ProductData.objects.filter(category="Camera")
    prod_dict = {}
    for product in products:
        qr_obj = Inventory.objects.filter(product=product.id)
        for object in qr_obj:
            quantity_in_stock = object.quantity_in_stock
        prod_dict[product.sku] = {
            "prod_name": product.prod_name,
            "price": product.price,
            "quantity": quantity_in_stock
        }
    
    if 'sort_by_price' in request.POST:
        sorted_by_price = dict(sorted(prod_dict.items(), key=lambda x: x[1]["price"]))
        return render(request, 'cameras.html', {"products": sorted_by_price})
    
    if 'sort_by_name' in request.POST:
        sorted_by_name = dict(sorted(prod_dict.items(), key=lambda x: x[1]["prod_name"]))
        return render(request, 'cameras.html', {"products": sorted_by_name})
    
    return render(request, 'cameras.html', {"products": prod_dict})

def monitors(request):
    products = ProductData.objects.filter(category="Monitor")
    prod_dict = {}
    for product in products:
        qr_obj = Inventory.objects.filter(product=product.id)
        for object in qr_obj:
            quantity_in_stock = object.quantity_in_stock
        prod_dict[product.sku] = {
            "prod_name": product.prod_name,
            "price": product.price,
            "quantity": quantity_in_stock
        }
    
    if 'sort_by_price' in request.POST:
        sorted_by_price = dict(sorted(prod_dict.items(), key=lambda x: x[1]["price"]))
        return render(request, 'monitors.html', {"products": sorted_by_price})
    
    if 'sort_by_name' in request.POST:
        sorted_by_name = dict(sorted(prod_dict.items(), key=lambda x: x[1]["prod_name"]))
        return render(request, 'monitors.html', {"products": sorted_by_name})
    
    return render(request, 'monitors.html', {"products": prod_dict})

def controllers(request):
    products = ProductData.objects.filter(category="Controller")
    prod_dict = {}
    for product in products:
        qr_obj = Inventory.objects.filter(product=product.id)
        for object in qr_obj:
            quantity_in_stock = object.quantity_in_stock
        prod_dict[product.sku] = {
            "prod_name": product.prod_name,
            "price": product.price,
            "quantity": quantity_in_stock
        }
    
    if 'sort_by_price' in request.POST:
        sorted_by_price = dict(sorted(prod_dict.items(), key=lambda x: x[1]["price"]))
        return render(request, 'controllers.html', {"products": sorted_by_price})
    
    if 'sort_by_name' in request.POST:
        sorted_by_name = dict(sorted(prod_dict.items(), key=lambda x: x[1]["prod_name"]))
        return render(request, 'controllers.html', {"products": sorted_by_name})
    
    return render(request, 'controllers.html', {"products": prod_dict})

def routers(request):
    products = ProductData.objects.filter(category="Router")
    prod_dict = {}
    for product in products:
        qr_obj = Inventory.objects.filter(product=product.id)
        for object in qr_obj:
            quantity_in_stock = object.quantity_in_stock
        prod_dict[product.sku] = {
            "prod_name": product.prod_name,
            "price": product.price,
            "quantity": quantity_in_stock
        }
    
    if 'sort_by_price' in request.POST:
        sorted_by_price = dict(sorted(prod_dict.items(), key=lambda x: x[1]["price"]))
        return render(request, 'routers.html', {"products": sorted_by_price})
    
    if 'sort_by_name' in request.POST:
        sorted_by_name = dict(sorted(prod_dict.items(), key=lambda x: x[1]["prod_name"]))
        return render(request, 'routers.html', {"products": sorted_by_name})
    
    return render(request, 'routers.html', {"products": prod_dict})

from django.shortcuts import render
from django.http import HttpResponse

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        if query:
            try:
                all_products_set = ProductData.objects.all()
                products = []
                for item in all_products_set:
                    temp_prod = []
                    temp_prod.append(item.category) 
                    temp_prod.append(item.prod_name)
                    products.append(temp_prod)
                
                filtered_products = []
                for item in products:
                    if query in item[1]:  # Assuming the name is at index 1 of the item
                        filtered_products.append(item[1])
                    if query in item[0]:
                        if item[1] not in filtered_products:
                            filtered_products.append(item[1])
                result = {}
                for item in filtered_products:
                    product_obj = ProductData.objects.filter(prod_name=item)
                    for prod_item in product_obj:
                        id = prod_item.id
                        inventory_obj = Inventory.objects.filter(product= id)
                        for i in inventory_obj:
                            quantity = i.quantity_in_stock
                        result[item] = {"price":prod_item.price, "sku":prod_item.sku, "quantity":quantity,}
                      
                context = {'products': result}
                return render(request, 'search_res.html', context)
            except Exception as e:
                print(e)
                return HttpResponse("Error processing your request.")
        else:
            return render(request, 'search_res.html')
    
    else:
        return render(request, 'search_res.html')

@login_required(login_url='login')
def cart(request):
    total_price = 0
    context = {}
    items_dict = {}
    placed_orders = {}
    completed_orders = {}
    user = request.user.id
    try:
        if request.method == "POST":
            additional_message = None
            if 'order_button' in request.POST:
                order_items = OrderItem.objects.filter(order_id=None, customer_id=user)
                total_price = 0
                for order_item in order_items:
                    total_price += order_item.quantity * order_item.price
                    inventory_obj = Inventory.objects.filter(product_id = order_item.product_id)
                    for object in inventory_obj:
                        print(object)
                        object.quantity_in_stock = object.quantity_in_stock - order_item.quantity
                        object.save()
                new_order = OrderData(order_status="placed", total_price=total_price, customer_id=user)
                new_order.save()
                for order_item in order_items:
                    order_item.order_id = new_order.id
                    order_item.save()
                return redirect('Cart')
            else:
                quantity = request.POST.get("quantity")
                if quantity is not None:
                    quantity = int(quantity)
                product_id = request.POST.get("product_id")
                inventory_obj = Inventory.objects.filter(product_id = product_id)
                for object in inventory_obj:
                    quantity_in_stock = object.quantity_in_stock
                if product_id is not None:
                    product_id = int(product_id)
                if quantity <= 0:
                    OrderItem.objects.filter(product_id = product_id, order_id = None).delete()
                elif quantity > quantity_in_stock:
                    additional_message = "There is not enough in stock"
                else:
                    OrderItem.objects.filter(product_id=product_id, order_id=None).update(quantity=quantity)
                for order_item in OrderItem.objects.filter(order_id=None, customer_id = user ):
                    product_name = order_item.product.prod_name
                    sku = order_item.product.sku
                    items_dict[product_name] = {"price":order_item.quantity*order_item.price,"sku":sku,
                                                "quantity":order_item.quantity, "product_id": order_item.product_id,}
                    total_price += items_dict[product_name]["price"]
                for placed_item in OrderData.objects.filter(order_status = "placed", customer_id = user):
                    for order_item in OrderItem.objects.filter(order_id=placed_item.id, customer_id = user ):
                        product_name = order_item.product.prod_name
                        sku = order_item.product.sku
                        placed_orders[product_name] = {"price":order_item.quantity*order_item.price,"sku":sku,
                                            "quantity":order_item.quantity, "product_id": order_item.product_id}
                for completed_item in OrderData.objects.filter(order_status = "completed", customer_id = user):
                    for order_item in OrderItem.objects.filter(order_id=completed_item.id, customer_id = user ):
                        product_name = order_item.product.prod_name
                        sku = order_item.product.sku
                        completed_orders[product_name] = {"price":order_item.quantity*order_item.price,"sku":sku,
                                            "quantity":order_item.quantity, "product_id": order_item.product_id}
                context = {
                    'order_items': items_dict,
                    'total_price': total_price,
                    'placed_orders': placed_orders,
                    'completed_orders': completed_orders,
                    "additional_message": additional_message
                    }
                print(context)
        else:
            print('asdddddddddddddddddddddddddddd')
            for order_item in OrderItem.objects.filter(order_id=None, customer_id = user ):
                    product_name = order_item.product.prod_name
                    sku = order_item.product.sku
                    items_dict[product_name] = {"price":order_item.quantity*order_item.price,"sku":sku,
                                                "quantity":order_item.quantity, "product_id": order_item.product_id,}
                    total_price += items_dict[product_name]["price"]
            for placed_item in OrderData.objects.filter(order_status = "placed", customer_id = user):
                for order_item in OrderItem.objects.filter(order_id=placed_item.id, customer_id = user ):
                    product_name = order_item.product.prod_name
                    sku = order_item.product.sku
                    placed_orders[product_name] = {"price":order_item.quantity*order_item.price,"sku":sku,
                                            "quantity":order_item.quantity, "product_id": order_item.product_id}
            for completed_item in OrderData.objects.filter(order_status = "completed", customer_id = user):
                for order_item in OrderItem.objects.filter(order_id=completed_item.id, customer_id = user ):
                    product_name = order_item.product.prod_name
                    sku = order_item.product.sku
                    completed_orders[product_name] = {"price":order_item.quantity*order_item.price,"sku":sku,
                                            "quantity":order_item.quantity, "product_id": order_item.product_id}
            context = {
                'order_items': items_dict,
                'total_price': total_price,
                'placed_orders': placed_orders,
                'completed_orders': completed_orders,
                }
    except Exception as e:
        print(e)
    return render(request, 'Cart.html', context)