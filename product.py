
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
       
    #metod za prikaz info o proizvodu
    def display_info(self):
        print(f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}")

    #metod za azuriranje kolicine
    def update_quantity(self, new_quantity):
        if new_quantity:
            self.quantity = new_quantity
        return self.quantity

    def get_price(self):
        return self.price

