
from product import Product
from product_manager import ProductManager

prm1 = ProductManager([])


prm1.add_product("Laptop", 1200, 10)
prm1.add_product("Mouse", 50, 50)  
prm1.add_product("Monitor", 450, 5)
prm1.display_products()
prm1.total_value()


