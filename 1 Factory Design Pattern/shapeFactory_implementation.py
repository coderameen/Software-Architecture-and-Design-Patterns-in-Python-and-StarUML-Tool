class Shape:
    def draw(self): pass

class Circle(Shape):
    def draw(self): return "Drawing Circle"

class Square(Shape):
    def draw(self): return "Drawing Square"

class Rectangle(Shape):
    def draw(self): return "Drawing Rectangle"

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        shapes = {'circle': Circle, 'square': Square, 'rectangle': Rectangle}
        return shapes.get(shape_type.lower())()

# Client Code
shape1 = ShapeFactory.create_shape('circle')
shape2 = ShapeFactory.create_shape('square')

print(shape1.draw())  # Output: Drawing Circle
print(shape2.draw())  # Output: Drawing Square
