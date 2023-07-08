from abc import ABC

class Drawable(ABC):

    def draw(self):
        raise NotImplemented()
    
    def hi(self):
        print("hi")

class Line(Drawable):
    pass
    # def draw(self):
    #     print("Draw line")

class Rectangle(Drawable):
    """
    Rectangle class to create perfect rectangles
    """

    width: int
    height: int

    __internal: int = None

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def calc_perimeter(self):
        """
        Calcualtes perimeter of rectangle
        """
        return self.__calc()

    def __calc(self):
        return (self.width + self.height) * 2 # formula for calcualting perimeter
    
    def draw(self):
        print("Draw rectangle")
    
    @property
    def perimeter(self):
        return self.__calc()

class Square(Rectangle):

    def __init__(self, width: int) -> None:
        super().__init__(width, width)
    
    @property
    def perimeter(self):
        return (self.width + self.height) * 4
    
    def draw(self):
        print("Draw Square")


def draw_screen(figure: Drawable):
    figure.draw()

rect = Rectangle(4,6)
square = Square(4)
line = Line()
draw_screen(rect)
draw_screen(square)
draw_screen(line)
# print(rect._Rectangle__calc())
# print(dir(rect))

# print(rect.calc_perimeter())
# print(square.perimeter)
# print(square.calc_perimeter)