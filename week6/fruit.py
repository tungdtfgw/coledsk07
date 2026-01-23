class Fruit:
    def __init__(self, name, price):
        self.name = name        # property, not attribute
        self.price = price

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

list_fruits = [
    Fruit("Apple", 1.5),
    Fruit("Banana", 0.8),
    Fruit("Cherry", 2.0),
    Fruit('Mango', 1.2),
    Fruit('Orange', 1.0)
]

if __name__ == "__main__":
    apple = Fruit("Apple", 1.5)
    print(apple.name)   # Output: Apple
    print(apple.price)  # Output: 1.5