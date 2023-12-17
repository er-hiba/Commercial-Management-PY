class Product():
    __num_products = 0
    
    def __init__(self, ref, purchase_price, selling_price, designation, stock=0):
        self.__ref = ref
        self.__purchase_price = purchase_price
        self.__selling_price = selling_price
        self.__stock = stock
        self.__designation = designation
        Product.__num_products += 1

    def get_ref(self):
        return self.__ref

    def get_purchase_price(self):
        return self.__purchase_price

    def get_selling_price(self):
        return self.__selling_price

    def get_stock(self):
        return self.__stock

    def get_designation(self):
        return self.__designation

    @staticmethod
    def get_num_products():
        return Product.__num_products

    def set_ref(self, r):
        self.__ref = r

    def set_purchase_price(self, pa):
        self.__purchase_price = pa

    def set_selling_price(self, pv):
        self.__selling_price = pv

    def set_stock(self, stock):
        self.__stock = stock

    def set_designation(self, d):
        self.__designation = d

    def __str__(self):
        return(f"Product reference: {self.__ref}\n -Purchase Price: {self.__purchase_price}\n \
-Selling Price: {self.__selling_price}\n -Quantity: {self.__stock}\n \
-Designation: {self.__designation}\n")

    def __eq__(self, other):
        return self.__ref == other.__ref
