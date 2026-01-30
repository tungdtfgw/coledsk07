from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name  # property, not attribute
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name cannot be empty.")
        self.__name = value

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # Override __str__ method for better representation
    def __str__(self):
        return f"{self.name}"

if __name__ == "__main__":
    # Example usage (will raise error if instantiated directly)
    try:
        shape = Shape("Generic Shape")
    except TypeError as e:
        print(e)  # Cannot instantiate abstract class Shape with abstract methods area, perimeter