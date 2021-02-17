# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
def get_price():
    base_price = get_base_price()
    discount = get_discount_factor()
    price = base_price * discount
    return price

def get_base_price():
    quantity = int(input("Enter Quantity:" ))
    item_price = int(input("Enter Item Price:" ))
    base_price = quantity * item_price
    return base_price

def get_discount_factor():
    base_price = get_base_price()
    discount_factor = 0
    
    if base_price > 1000: 
        discount_factor = 0.95
    else: 
        discount_factor = 0.98
    return discount_factor

get_price()


