
from Cashier import *

print("----- EXAMPLE 1 -----")
products = []

shirt1 = Shirt()
shirt1.name = 'Blue Cotton Shirt'
shirt1.brand = 'BrandS'
shirt1.price = '$14.99'
shirt1.size = 'M'
shirt1.color = 'blue'
products.append(shirt1)

shirt2 = Shirt()
shirt2.name = 'White Cotton Shirt'
shirt2.brand = 'BrandS'
shirt2.price = '$15.99'
shirt2.size = 'M'
shirt2.color = 'white'
products.append(shirt2)

trousers1 = Trousers()
trousers1.name = 'Black Cotton Trousers'
trousers1.brand = 'BrandT'
trousers1.price = '$29.99'
trousers1.size = '50'
trousers1.color = 'black'
products.append(trousers1)

shoes1 = Shoe()
shoes1.name = 'Black Leather Shoes'
shoes1.brand = 'BrandS'
shoes1.price = '$59.99'
shoes1.size = '43'
shoes1.color = 'black'
products.append(shoes1)

jacket1 = SuitJacket()
jacket1.name = 'Black Cotton Suit Jacket'
jacket1.brand = 'BrandJ'
jacket1.price = '$99.99'
jacket1.size = '50'
jacket1.color = 'black'
products.append(jacket1)

cart_product_names = ['Blue Cotton Shirt', 'White Cotton Shirt', 'Black Cotton Trousers', 'Black Leather Shoes','Black Cotton Suit Jacket'
                      ]
cart = []

for name in cart_product_names:
    for product in products:
        if name == product.name:
            cart.append(product)

cashier = Cashier(cart, '2022-11-16 12:35:45')
cashier.printReciept()


