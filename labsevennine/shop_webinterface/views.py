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
            return render(request, 'shop.html')
        except Exception as e:
            print("ordering", e)
            return HttpResponse("Error processing your request.")
    else:
        return HttpResponse("Error processing your request.")

def sensors(request):
    products = ProductData.objects.filter(category="Sensor")
    print (products)
    return render(request, 'sensors.html', {"products": products})

def cameras(request):
    products = ProductData.objects.filter(category="Camera")
    return render(request, 'sensors.html', {"products": products})

def monitors(request):
    products = ProductData.objects.filter(category="Monitor")
    return render(request, 'sensors.html', {"products": products})

def controllers(request):
    products = ProductData.objects.filter(category="Controller")
    return render(request, 'sensors.html', {"products": products})

def routers(request):
    products = ProductData.objects.filter(category="Router")
    return render(request, 'sensors.html', {"products": products})

@login_required(login_url='login')
def cart(request):
    email = request.user.email
    customer_id = request.user.id
    context = {}
    total_price = 0
    
    if request.method == 'POST':
        try:
            quantity = request.POST.get("quantity")
            if quantity is not None:
                quantity = int(quantity)
            product_id = request.POST.get("product_id")
            if product_id is not None:
                product_id = int(product_id)       
                
            order_items = OrderItem.objects.filter(customer_id=customer_id, order_id=None)
            for i in order_items:
                if i.quantity <= 0:
                    i.delete()
                else:
                    i.save()

            context = {'order_items': order_items}
            total_price = sum([item.product.price * item.quantity for item in order_items])
            
            if 'order_button' in request.POST and len(order_items) > 0:
                order = OrderData.objects.create(customer_id=customer_id, order_status='Placed', total_price=total_price)
                for item in order_items:
                    item.order_id = order.id
                    item.save()
                context['placed_orders'] = OrderData.objects.filter(customer_id=customer_id, order_status='Placed')
                context['completed_orders'] = OrderData.objects.filter(customer_id=customer_id, order_status='Completed')
                return render(request, 'cart.html', context)
            
            context['placed_orders'] = OrderData.objects.filter(customer_id=customer_id, order_status='Placed')
            context['completed_orders'] = OrderData.objects.filter(customer_id=customer_id, order_status='Completed')
            return render(request, 'cart.html', context)
        except Exception as e:
            print("cart", e)
            return HttpResponse("Error processing your request.")
    else:
        order_items = OrderItem.objects.filter(customer_id=customer_id, order_id=None)
        context = {'order_items': order_items}
        total_price = sum([item.product.price * item.quantity for item in order_items])
        context['total_price'] = total_price
        context['placed_orders'] = OrderData.objects.filter(customer_id=customer_id, order_status='Placed')
        context['completed_orders'] = OrderData.objects.filter(customer_id=customer_id, order_status='Completed')
        return render(request, 'cart.html', context)

