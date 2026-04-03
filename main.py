from product import Product
from product_manager import ProductManager


def main() -> None:
    manager = ProductManager()

    manager.add_product(Product("Laptop1", 1200.0, 5))
    manager.add_product(Product("Mouse2", 25.5, 20))
    manager.add_product(Product("Keyboard3", 75.0, 10))
    manager.add_product(Product("Monitor4", 250.0, 7))
    manager.add_product(Product("Headphones5", 45.0, 15))


if __name__ == "__main__":
    main()
