class Product:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price

    def set_price(self, new_price):
        self._price = new_price


class Customer:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age
        

class Sale:
    def __init__(self, id, product, customer, date):
        self._id = id
        self._product = product
        self._customer = customer
        self._date = date

    def make_sale(self):
        if self._product._price > self._customer._age:
            print("The customer is too young to buy this product.")
        else:
            self._product.set_price(self._product._price - 5)
            print(f"The sale was successful. The price of the product {self._product._name} was reduced to {self._product._price}.")

            
# 4 OOP принципи

product1 = Product(id=1, name="Phone", price=150.0)
product2 = Product(id=2, name="Laptop", price=800.0)

customer1 = Customer(id=1, name="Ivan", age=30)
customer2 = Customer(id=2, name="Petar", age=25)

sale1 = Sale(id=1, product=product1, customer=customer1, date="2022-03-10")
sale2 = Sale(id=2, product=product2, customer=customer2, date="2022-03-15")

sale1.make_sale()
sale2.make_sale()

print(sale1.id)
print(sale1.product._name)
print(sale1.customer._name)
print(sale1.date)