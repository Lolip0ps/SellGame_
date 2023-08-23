from django.shortcuts import render
from .models import *
from catalog.models import NameGame, KeyGame
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            user_email = order.email
            message = ''
            for item in cart:
                product = item['product']
                quantity = item['quantity']
                name_key = NameGame.objects.get(name=product).id
                keys = KeyGame.objects.filter(name=name_key)[:quantity]
                for num in keys:
                    message += str(item['product']) + ' : ' + num.key + '\n'
                    KeyGame.objects.filter(id=num.id).delete() #Вернуть перед релизом
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            send_mail('Спасибо за покупку', message, 'Lolipops1236q@yandex.ru', [user_email],
                      fail_silently=False)
            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'order/create.html', {'cart': cart, 'form': form})
