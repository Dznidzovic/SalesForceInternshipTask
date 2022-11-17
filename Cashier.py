from Discounts import *
import datetime



class Cashier:
    def __init__(self, cart, date):
        self._cart = cart
        self._date = date

    def printReciept(self):
        subtotal = 0
        totaldiscount = 0

        # create a datetime object from date string passed, than find the day of the week
        date_for_date_time = self._date.split(" ")[0].split("-")
        day_of_the_week = datetime.datetime(int(date_for_date_time[0]), int(date_for_date_time[1]),
                                            int(date_for_date_time[2])).weekday()

        print("Date: {}".format(self._date))
        print("---Products---")
        print('\n')
        for prod in self._cart:
            for discount in Discount.__subclasses__():
                prod_price = float(prod.price[1:])

                prod_discount = discount.calculate_discount(self, prod, self._cart, day_of_the_week)

                # We don't want to print anything for discount None as that means the discount function did not match
                # the product
                if prod_discount is not None:
                    subtotal += prod_price
                    totaldiscount += round(prod_price * prod_discount,2)
                    print(prod.name, "-", prod.brand)
                    print(prod.price)
                    print("#discount {}% -${}".format(prod_discount * 100, format(round(prod_price * prod_discount, 2),'0.2f')))
                    print("\n")
        print("--------------------------------")
        print("SUBTOTAL: $",round(subtotal,3))
        print("DISCOUNT: -$",format(totaldiscount,'.2f'))
        print("TOTAL: $",format(subtotal-totaldiscount,'.2f'))