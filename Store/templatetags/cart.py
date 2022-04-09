from django import template

register = template.Library()

@register.filter(name='is_in_cart')#ei nam ta holo kon name template e use korbo oi nam,
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')#ei nam ta holo kon name template e use korbo oi nam,

def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            quantity = cart.get(id)
            return quantity
    return 0


@register.filter(name='total_price')
def total_price(product, cart):
    product_price = product.Unit_price
    product_quantity = cart_quantity(product, cart)
    return product_price * product_quantity

@register.filter(name='cart_total_price')
def cart_total_price(products, cart):
    sum= 0
    for p in products:
        a=total_price(p, cart)
        sum+=a
    return sum 