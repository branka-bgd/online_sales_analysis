class Cart:
    def __init__(self):
        self.cart_items = {}  # {Product: quantity}

    def add_item(self, product, quantity):
        """Adds a product to the cart or updates its quantity."""
        if quantity > 0:
            self.cart_items[product] = self.cart_items.get(product, 0) + product.quantity
            print(f"Added {product.quantity} {product.name} to the cart.")

    def total_amount(self):
        # Calculate total spent using Product price and quantity
        return sum(product.price * product.quantity for product, quantity in self.cart_items.items())
        
    def view_cart(self):
        """Displays items and total."""
        print("Cart:")
        for product, product.quantity in self.cart_items.items():
            print(f"\t{product.name}: {product.quantity}, price per piece {product.price:.2f}")
        print(f"Total amount: {self.total_amount():.2f}")