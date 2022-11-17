from Cashier import *

print("----- EXAMPLE 3 -----")
products = []

trousers1 = Trousers()
trousers1.name = 'Red Linen Trousers'
trousers1.brand = 'BrandT'
trousers1.price = '$49.99'
trousers1.size = '56'
trousers1.color = 'red'
products.append(trousers1)

shoes1 = Shoe()
shoes1.name = 'Red Suede Shoes'
shoes1.brand = 'BrandS'
shoes1.price = '$59.99'
shoes1.size = '44'
shoes1.color = 'red'
products.append(shoes1)

shoes2 = Shoe()
shoes2.name = 'Black Suede Shoes'
shoes2.brand = 'BrandS'
shoes2.price = '$59.99'
shoes2.size = '44'
shoes2.color = 'black'
products.append(shoes2)

jacket1 = SuitJacket()
jacket1.name = 'Red Linen Suit Jacket'
jacket1.brand = 'BrandJ'
jacket1.price = '$99.99'
jacket1.size = '56'
jacket1.color = 'red'
products.append(jacket1)

shirt1 = Shirt()
shirt1.name = 'White Linen Shirt'
shirt1.brand = 'BrandS'
shirt1.price = '$29.99'
shirt1.size = 'L'
shirt1.color = 'white'
products.append(shirt1)

cart_product_names = ['Red Linen Trousers', 'Red Suede Shoes', 'Black Suede Shoes', 'Red Linen Suit Jacket','White Linen Shirt']
cart = []

for name in cart_product_names:
    for product in products:
        if name == product.name:
            cart.append(product)

cashier = Cashier(cart, '2022-11-15 12:35:45')
cashier.printReciept()
