
class Product :
    """Represents a product with name , price, and quantity, and an inventory to manage multiple products."""
    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self._name = name
        self._price = price
        self._quantity = quantity
    
    
    """Encapsulates product attributes and provides methods to access and modify them safely."""

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value

    def get_value(self) -> float:
        """Returns the total value of the product stock."""
        return self._price * self._quantity
    


        
class Inventory :
    """Manages a collection of Product objects, and allow stock management operations."""
    def __init__(self):
        self._products = {}
    

    """Adds a new product to the inventory or increases quantity if it already exists."""
    def add_product(self, product: Product):
        if product.name in self._products:
            self._products[product.name].quantity += product.quantity # Increase quantity if product exists
        else:
            self._products[product.name] = product # Add new product

    """Removes a specified quantity of a product , or removes the product entirely if quantity exceeds or equals current stock."""
    def remove_product(self, product_name: str, quantity: int): # Removes specified quantity of a product by name
        if product_name not in self._products:
            raise ValueError(f"Product '{product_name}' not found in inventory")

        if quantity < 0: 
            raise ValueError("Quantity to remove cannot be negative") 

        product = self._products[product_name]
        
        if product.quantity > quantity: # Reduce quantity if enough stock
            product.quantity -= quantity

        elif product.quantity == quantity:
            del self._products[product_name] # Remove product entirely if quantity matches

        else:
            raise ValueError("Not enough stock to remove the requested quantity")

    """Returns the total value of all products in the inventory."""
    def get_total_value(self) -> float:
        total_value = 0.0
        for product in self._products.values():
            total_value += product.get_value()
        return total_value




# Unit tests for the Inventory and Product classes
"""import unittest

class TestInventorySystem(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
        self.apple = Product("apple", 2.0, 10)
        self.banana = Product("banana", 1.5, 5)
        self.inv.add_product(self.apple)
        self.inv.add_product(self.banana)

    def test_total_value(self):
        self.assertEqual(self.inv.get_total_value(), 27.5)

    def test_remove_partial_quantity(self):
        self.inv.remove_product("apple", 3)
        self.assertEqual(self.inv.get_total_value(), 21.5)  # Correct expected value

    def test_remove_entire_product(self):
        self.inv.remove_product("banana", 5)
        self.assertNotIn("banana", self.inv._products)

    def test_remove_more_than_available(self):
        with self.assertRaises(ValueError):
            self.inv.remove_product("apple", 20)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            Product("orange", -1.0, 5)

if __name__ == "__main__":
    unittest.main()"""