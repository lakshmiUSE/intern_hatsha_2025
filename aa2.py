class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items.remove(product)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        print("Total Price:", total)


p1 = Product("Phone", 15000)
p2 = Product("Headphones", 2000)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
cart.total_price()
