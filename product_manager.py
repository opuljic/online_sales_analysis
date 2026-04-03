from product import Product


class ProductManager:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            return "No products available."
        return "\n".join(product.display_info() for product in self.products)

    def display_total_value(self):
        return sum(product.price * product.quantity for product in self.products)

    def remove_product_by_name(self, name):
        for index, product in enumerate(self.products):
            if product.name == name:
                del self.products[index]
                return True
        return False
