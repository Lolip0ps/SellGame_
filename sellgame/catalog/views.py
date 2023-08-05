from django.shortcuts import render, HttpResponse, get_object_or_404
from cart.forms import CartAddProductForm
from .models import *


def product_list(request, category_slug=None):
    name_key = NameGame.objects.all()
    for name in name_key:  # Количество ключей в каталоге
        q_name = KeyGame.objects.filter(name=name).count()
        Product.objects.filter(connect=name.id).update(stock=q_name)

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_published=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        "category": category,
        "categories": categories,
        "products": products
    }
    return render(request, 'catalog/list.html', context=context)


# def show_post(request, post_id):
#     return HttpResponse(f"Отображение игры с id = {post_id}")

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_published=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'catalog/detail.html', context=context)
