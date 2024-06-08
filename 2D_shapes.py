import math
import pytest
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, point1_x, point1_y, point2_x, point2_y, point3_x, point3_y):
        self.point1_x = point1_x
        self.point1_y = point1_y
        self.point2_x = point2_x
        self.point2_y = point2_y
        self.point3_x = point3_x
        self.point3_y = point3_y

    def perimeter(self):
        
    
        side1 = math.sqrt((self.point1_x - self.point2_x) ** 2 + (self.point1_y - self.point2_y) ** 2)
        side2 = math.sqrt((self.point1_x - self.point3_x) ** 2 + (self.point1_y - self.point3_y) ** 2)
        side3 = math.sqrt((self.point2_x - self.point3_x) ** 2 + (self.point2_y - self.point3_y) ** 2)

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        return side1 + side2 + side3

    def area(self):
        
        s = float(self.perimeter()) / 2 
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area


class Rectangle(Shape):
    def __init__(self, top_right_x, top_right_y, bottom_left_x,  bottom_left_y): 
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.bottom_left_x = bottom_left_x
        self.bottom_left_y = bottom_left_y
    
    def perimeter(self):
        return 2 * ((self.top_right_x - self.bottom_left_x) + (self.top_right_y - self.bottom_left_y))
    
    def area(self):
        return (self.top_right_x - self.bottom_left_x) * (self.top_right_y - self.bottom_left_y)

class Square(Rectangle):
    def __init__(self, side): 
        
        self.side = side
        super().__init__(side, side, 0, 0)

class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * (self.radius ** 2)


def main():
    """
    The main function. It handles user input, creates instances of the 
    respective shapes, calculates their perimeters and areas, and prints the results. It continues to run until 
    the user chooses to exit.
    """
    while True:
        user_choice = input("1 - Square\n"
                                    "2 - Rectangle\n"
                                    "3 - Circle\n"
                                    "0 - Exit\n"
                                    "Your choice: ")
        
        match user_choice:
            case '1':
                user_choice = 'Square'

                side = int(input("Square data:\n"
                                    "Enter side: "))
                
                square = Square(side)

                perimeter = square.perimeter()
                area = square.area()

                print(f"Square Perimeter: {perimeter}")
                print(f"Square Area: {area}")

            case '2':
                user_choice = 'Rectangle'

                top_right_x = int(input("Rectangle data:\n"
                                    "Enter top right corner x: "))
                top_right_y = int(input("top right corner y: "))
                bottom_left_x = int(input("bottom left corner x: "))
                bottom_left_y = int(input("bottom left corner y: "))

                rectangle = Rectangle(top_right_x, top_right_y, bottom_left_x,  bottom_left_y)

                perimeter = rectangle.perimeter()
                area = rectangle.area()

                print(f"Rectangle Perimeter: {perimeter}")
                print(f"Rectangle Area: {area}")

            case '3':
                user_choice = 'Circle'
                
                center_x = int(input("Circle data:\n"
                                    "Enter center x: "))
                center_y = int(input("center y: "))
                radius = int(input("radius: "))

                circle = Circle(center_x, center_y, radius)

                perimeter = circle.perimeter()
                area = circle.area()

                print(f"Circle Perimeter: {perimeter}")
                print(f"Circle Area: {area}")

            case '0':
                print(f"Goodbye!")
                break   

            case _:
                print("Incorrect input. Please enter a valid option (0-3).")
                continue

def test_square():
    square = Square(3)
    assert square.perimeter() == 12
    assert square.area() == 9

def test_rectangle():
    rectangle = Rectangle(2, 2, 1, 1)
    assert rectangle.perimeter() == 4
    assert rectangle.area() == 1

def test_circle():
    circle = Circle(3, 7, 5)
    assert circle.perimeter() == pytest.approx(2 * math.pi * 5)
    assert circle.area() == pytest.approx(math.pi * 5**2)                      

def test_rectagle_attributes():
    rectangle = Rectangle(2, 2, 1, 1)
    assert rectangle.top_right_x == 2
    assert rectangle.top_right_y == 2
    assert rectangle.bottom_left_x == 1
    assert rectangle.bottom_left_y == 1

def test_square_attributes():
    square = Square(2)
    assert square.side == 2
    assert square.top_right_x == 2
    assert square.top_right_y == 2
    assert square.bottom_left_x == 0
    assert square.bottom_left_y == 0

def test_triangle_attributes():
    triangle = Triangle(0, 1, 1, 1, 1, 0)
    assert triangle.point1_x == 0
    assert triangle.point1_y == 1
    assert triangle.point2_x == 1
    assert triangle.point2_y == 1
    assert triangle.point3_x == 1
    assert triangle.point3_y == 0


def test_triangle():
    triangle = Triangle(0, 1, 1, 1, 1, 0)
    assert triangle.perimeter() == 3.414213562373095
    assert triangle.area() == pytest.approx(0.5)
    

if __name__ == "__main__":
    main()
