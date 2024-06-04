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

class Square(Shape):
    def __init__(self, side): 
        self.side = side
    
    def perimeter(self):
        return 4 * self.side
    
    def area(self):
        return self.side ** 2


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
            
if __name__ == "__main__":
    main()