# Base Coffee class
class Coffee:
    def cost(self):
        return 5  # Base cost of coffee

# Base Decorator class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # Add cost of milk

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5  # Add cost of sugar

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1.5  # Add cost of whipped cream

# Client Code
if __name__ == "__main__":
    coffee = Coffee()  # Basic coffee
    coffee_with_milk = MilkDecorator(coffee)  # Coffee with milk
    coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)  # Coffee with milk and sugar
    coffee_full = WhippedCreamDecorator(coffee_with_milk_sugar)  # Coffee with milk, sugar, and whipped cream

    print(f"Total cost: ${coffee_full.cost():.2f}")  # Output: Total cost: $8.00
