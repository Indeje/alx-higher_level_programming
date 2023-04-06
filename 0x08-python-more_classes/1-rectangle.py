#!/usr/bin/python3

"""
    Module with rectangle class
"""


class Rectangle:
    """
        A class that defines a rectangle
    """

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
