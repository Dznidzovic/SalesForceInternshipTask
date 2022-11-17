from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self):
        self._name = ''
        self._brand = ''
        self._size = ''
        self._price = ''
        self._color = ''

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        self._brand = value

    @abstractmethod
    def get_size(self):
        return self._size

    @abstractmethod
    def set_size(self, value):
        self._size = value

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value

    name = property(get_name, set_name)
    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)
    price = property(get_price, set_price)
    color = property(get_color, set_color)


class Shirt(Product):

    def get_size(self):
        return self._size

    def set_size(self, value):
        sizes = ['XS', 'S', 'M', 'L', 'XL', '2XL']
        nonExistingSize = False
        for size in sizes:
            if value == size:
                nonExistingSize = True
        if not nonExistingSize:
            raise Exception("Size input invalid!")
        else:
            self._size = value

    size = property(get_size, set_size)


class Shoe(Product):
    def get_size(self):
        return self._size

    def set_size(self, value):
        try:
            shoe_size = int(value)
        except ValueError as vr:
            raise Exception("Invalid Shoe Size!")

        if 39 <= shoe_size <= 46:
            self._size = shoe_size
        else:
            raise Exception("Shoe sizes must be between 39 and 46!")

    size = property(get_size, set_size)


class SuitJacket(Product):
    def get_size(self):
        return self._size

    def set_size(self, value):
        try:
            jacket_size = int(value)
        except ValueError as vr:
            raise Exception("Invalid Jacket Size!")
        if jacket_size % 2 != 0:
            raise Exception("Jacket size must be an even number!")
        elif jacket_size < 42 or jacket_size > 66:
            raise Exception("Jacket size must be between 42 and 46!")
        self._size = jacket_size

    size = property(get_size, set_size)


class Trousers(Product):
    def get_size(self):
        return self._size

    def set_size(self, value):
        try:
            jacket_size = int(value)
        except ValueError as vr:
            raise Exception("Invalid Jacket Size!")
        if jacket_size % 2 != 0:
            raise Exception("Jacket size must be an even number!")
        elif jacket_size < 42 or jacket_size > 66:
            raise Exception("Jacket size must be between 42 and 46!")
        self._size = jacket_size

    size = property(get_size, set_size)
