#!/usr/bin/python3

"""
    Module with rectangle class
"""


class Rectangle:
    """
        A class that defines a rectangle
    """

    number_of_instances = 0     # Public Class Attribute

    def __init__(self, width=0, height=0) -> None:
        """
            Checks the parameters and initializes values
            Args:
                width (:obj:`int`, optional): The width of the Rectangle.
                height (:obj:`int`, optional): The height of the Rectangle.
        """

        if self.__check_width(width) and self.__check_height(height):
            self.__width = width
            self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self) -> str:
        """
            Custom __str__ method
        """

        rect_str = ''
        if self.height == 0 or self.width == 0:
            return rect_str
        for y in range(self.height):
            for x in range(self.width):
                rect_str += '#'

            if y != (self.height - 1):
                rect_str += '\n'
        return rect_str

    def __repr__(self) -> str:
        """
            Custom __repr__ method
        """

        rect_repr = ''
        rect_repr += type(self).__name__
        rect_repr += f'({self.width}, {self.height})'
        return rect_repr

    def __del__(self):
        """
            Destructor method
        """

        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
            Width property getter
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
            Width property setter
        """

        self.__check_width(value)
        self.__width = value

    @property
    def height(self):
        """
            Height property getter
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
            Height property setter
        """

        self.__check_height(value)
        self.__height = value

    def __check_width(self, width):
        """
            Check width parameter
            Args:
                Width (int) - Rectangle width
        """

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        return True

    def __check_height(self, height):
        """
            Check height parameter
            Args:
                Height (int) - Rectangle height
        """

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        return True

    def area(self):
        """
            Returns rectangle area
        """

        return (self.height * self.width)

    def perimeter(self):
        """
            Returns rectangle perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0
        return ((self.height + self.width) * 2)
