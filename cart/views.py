from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404


def order_view(request):
    """ Renders order items in cart """
    return render(request, 'cart/shopping_cart.html')


def order_item(request, slug):
    """ Add item in quantity to cart"""

    try:
        qty = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if slug in list(cart.keys()):
            cart[slug] += qty
        else:
            cart[slug] = qty
        request.session['cart'] = cart
        return redirect('shopping_cart')
    except ValueError:
        # return a message to user on invaild input
        return redirect(reverse('books:book-details', args=[slug]))
