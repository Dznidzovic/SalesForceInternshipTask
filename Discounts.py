from abc import ABC, abstractmethod

from Products import *


class Discount(ABC):
    @abstractmethod
    def calculate_discount(self, product, products, date):
        pass


class ShirtDiscount(Discount):
    # dates are ints from 0 to 6 presenting(monday-tuesday)
    def calculate_discount(self, product, products, date):
        three_item_discount = 0
        tuesday_discount = 0

        if 'shirt' in product.name.lower():

            if len(products) >= 3:
                three_item_discount = 0.2
            if date == 1:
                tuesday_discount = 0.1

            final_product_discount = max(tuesday_discount, three_item_discount)
            return final_product_discount
        else:
            return


class ShoeDiscount(Discount):
    def calculate_discount(self, product, products, date):
        three_item_discount = 0
        tuesday_discount = 0

        if 'shoes' in product.name.lower():

            if len(products) >= 3:
                three_item_discount = 0.2
            if date == 1:
                tuesday_discount = 0.25

            final_product_discount = max(tuesday_discount, three_item_discount)
            return final_product_discount
        else:
            return


class TrousersDiscount(Discount):
    def calculate_discount(self, product, products, date):
        if 'trousers' in product.name.lower():

            if len(products) >= 3:
                return 0.2
            else:
                return 0
        else:
            return


class JacketDiscount(Discount):
    def calculate_discount(self, product, products, date):
        if 'jacket' in product.name.lower():

            if len(products) >= 3:
                return 0.2
            else:
                return 0
        else:
            return
