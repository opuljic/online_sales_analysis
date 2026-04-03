from product import Product
from product_manager import ProductManager


def main() -> None:
    manager = ProductManager()

    manager.add_product(Product("Laptop", 1200.0, 5))
    manager.add_product(Product("Mouse", 25.5, 20))
    manager.add_product(Product("Keyboard", 75.0, 10))

    print("All products:")
    print(manager.display_all_products())
    print()
    print(f"Total inventory value: {manager.display_total_value()}")


if __name__ == "__main__":
    main()
