
from product import Product

class ProductManager:

    def __init__(self, product_list):
        self.product_list = []
     
    #metod za dodavanje proizvoda      
    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.product_list.append(new_product)
    
    #metod za prikaz proizvoda
    def display_products(self):
        print(f"Product list: ")
        for product in self.product_list:
            print(f"\t{product.name} - price: {product.price}, quantity: {product.quantity}")
            
    #metod za prikaz ukupne vrednosti svih proizvoda
    def total_value(self):
        total_value = 0
        for pr in self.product_list:
            total_value += pr.price * pr.quantity
        print(f"\nTotal value of products: {total_value}")
         
    #metod za uklanjanje proizvoda
    def remove_product(self, name):
        product_found = False
        for product in self.product_list:
            if product.name == name:
                self.product_list.remove(product)
                product_found = True
                print(f"Removed product: {name}")
                break # Stop after the first match is removed
        if not product_found:
            print(f"Product {name} is not on list.")
