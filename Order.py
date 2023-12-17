import copy 
class Order():
    def __init__(self, date, product, quantity):
        self.__date = date
        self.__product = copy.copy(product)
        self.__quantity = quantity

    def get_date(self):
        return self.__date

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def set_date(self, d):
        self.__date = d

    def set_product(self, p):
        self.__product = p

    def set_quantity(self, q):
        self.__quantity = q

    def __str__(self):
        return(f"Order created on {self.__date}\n -Product: {str(self.__product)} -Quantity: {self.__quantity}\n")

    def __eq__(self, other):
        return self.__date == other.__date and self.__product == other.__product and self.__quantity == other.__quantity
