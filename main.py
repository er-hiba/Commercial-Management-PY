from Order import Order
from Product import Product

p1 = Product(12345, 200, 250,"Gaming Laptop",10 )

p2 = Product(54321, 200, 210,"Smartphone",20 )

o1 = Order("12/10/2023", p1, 150)
o2 = Order("12/10/2023", p1, 150)
o3 = Order("2/12/2023", p2, 200)

print(p1)
print(p2)

print(f"The number of products is {Product.get_num_products()}\n")

print(f"Product 1 reference = Product 2 reference: {p1 == p2}\n")

print(o1)
print(o2)
print(o3)

print(f"Order 1 = Order 2: {o1 == o2}\n")
