import random

from cart import Cart
from product import Product
from product_manager import ProductManager


def main() -> None:
    manager = ProductManager()

    manager.add_product(Product("Laptop", 1200.0, 5))
    manager.add_product(Product("Mouse", 25.5, 20))
    manager.add_product(Product("Keyboard", 75.0, 10))
    manager.add_product(Product("Monitor", 250.0, 7))
    manager.add_product(Product("Headphones", 45.0, 15))

    print("All products:")
    print(manager.display_all_products())
    print()
    print(f"Total inventory value: {manager.display_total_value()}")
    print()

    cart = Cart()
    available_products = manager.products
    selected_products = random.sample(available_products, 3)
    for product in selected_products:
        cart.add_product(product)

    print("Cart contents:")
    print(cart.display_cart())
    print()
    print(f"Cart total: {cart.calculate_total()}")


if __name__ == "__main__":
    main()
