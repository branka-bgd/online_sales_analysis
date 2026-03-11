
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
         
        
