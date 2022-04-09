from django import template

register = template.Library()

@register.filter(name="currency")
def currency(price):
    return str(price)+" ৳"

@register.filter(name="total_price_of_order")
def total_price_of_order(number, number1):
    return number * number1


@register.filter(name="available")
def available(number):
    if number == 1:
        return ' Only "1" product is available on stock'
    elif number==2:
        return ' Only "2" are available on stock'
    elif number == 3:
        return 'Only "3" products are available on stock'
    elif number > 3:
        return "Available"
    else:
        return 'Not Available'

 
@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 