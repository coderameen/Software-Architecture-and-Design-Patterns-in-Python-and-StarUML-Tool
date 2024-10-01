from abc import ABC, abstractmethod

# Abstract Products
class Shoes(ABC):
    @abstractmethod
    def type(self): pass

class Clothes(ABC):
    @abstractmethod
    def type(self): pass

# Concrete Products
class RunningShoes(Shoes):
    def type(self): return "Running Shoes"

class SwimmingSuit(Clothes):
    def type(self): return "Swimming Suit"

# Abstract Factory
class SportsFactory(ABC):
    @abstractmethod
    def create_shoes(self): pass

    @abstractmethod
    def create_clothes(self): pass

# Concrete Factory
class DecathlonFactory(SportsFactory):
    def create_shoes(self): return RunningShoes()
    def create_clothes(self): return SwimmingSuit()

# Client Code
factory = DecathlonFactory()
print(factory.create_shoes().type())  # Output: Running Shoes
print(factory.create_clothes().type())  # Output: Swimming Suit
