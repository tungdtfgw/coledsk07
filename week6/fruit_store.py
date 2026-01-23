# from file_name import ClassName
from fruit import Fruit, list_fruits


class FruitStore:
    def __init__(self, fruits):
        self.__fruits = fruits[:]  # Make a copy of the list

    def show_fruits(self):
        for fruit in self.__fruits:
            print(f"Fruit: {fruit.name}, Price: ${fruit.price:.2f}")

    def change_price(self, name, new_price):
        found = False
        for f in self.__fruits:
            if f.name == name:
                f.price = new_price
                found = True
        
        if not found:
            print(f"Fruit '{name}' not found in the store.")

if __name__ == "__main__":
    store = FruitStore(list_fruits)
    store.show_fruits()
    print("\nChanging price of Banana to $1.0\n")
    store.change_price("Banana", 1.0)
    store.show_fruits()

    store.change_price("Pineapple", 2.5)  # Fruit not in the store