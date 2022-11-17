from Products import *
from Discounts import *
from Cashier import *
import datetime

print("----- EXAMPLE 2 -----")
products = []

shirt1 = Shirt()
shirt1.name = 'Black Silk Shirt'
shirt1.brand = 'BrandS'
shirt1.price = '$29.99'
shirt1.size = 'L'
shirt1.color = 'black'
products.append(shirt1)

shirt2 = Shirt()
shirt2.name = 'White Silk Shirt'
shirt2.brand = 'BrandS'
shirt2.price = '$29.99'
shirt2.size = 'L'
shirt2.color = 'white'
products.append(shirt2)

cart_product_names = ['Black Silk Shirt','White Silk Shirt']
cart = []

for name in cart_product_names:
    for product in products:
        if name == product.name:
            cart.append(product)

cashier = Cashier(cart, '2022-11-15 12:35:45')
cashier.printReciept()
