class House:
    def __init__(self, foundation, roof, interior):
        self.foundation = foundation
        self.roof = roof
        self.interior = interior
    def __str__(self):
        return f"House with {self.foundation}, {self.roof}, and {self.interior}"

# Builder Interface
class HouseBuilder:
    def build(self):
        pass

# Wooden House Builder
class WoodenHouseBuilder(HouseBuilder):
    def build(self):
        return House("Wooden foundation", "Wooden roof", "Wooden interior")

# Brick House Builder
class BrickHouseBuilder(HouseBuilder):
    def build(self):
        return House("Concrete foundation", "Tile roof", "Modern interior")

# Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        return self.builder.build()

# Client Code
if __name__ == "__main__":
    # Build Wooden House
    wooden_house = Director(WoodenHouseBuilder()).construct_house()
    print(wooden_house)

    # Build Brick House
    brick_house = Director(BrickHouseBuilder()).construct_house()
    print(brick_house)
