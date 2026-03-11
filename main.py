
from product import Product
from product_manager import ProductManager
from cart import Cart

prm1 = ProductManager([])


#prm1.add_product("Laptop", 1200, 10)
#prm1.add_product("Mouse", 50, 50)  
#prm1.add_product("Monitor", 450, 5)
#prm1.display_products()
#prm1.total_value()

products = [
    Product("Laptop", 1200, 2),
    Product("Mouse", 20, 5),
    Product("Monitor", 250, 3)
]

my_cart = Cart()
for product in products:
    my_cart.add_item(product, 1)
my_cart.view_cart()
my_cart.total_amount()