#!/usr/bin/env python

from PIL import Image, ImageDraw
from random import choice

COLORS=("red", "green", "blue", "cyan", "magenta", "yellow") 

class xy():
    ''' a pair of x and y values which represent either a
        coordinate or a lengths in the x and y axes, which
        supports addition and subtraction '''

    def __init__(self, x, y):
        #assert isinstance(x, int) and isinstance(y, int), "x and y must be integers"
        #assert x >= 0 and y >= 0, "x and y must be positive"
        self.x(x)
        self.y(y)

    def x(self, x):
        ''' set x with data validation '''
        assert isinstance(x, int), "value is not an integer: {}".format(x)
        assert x >= 0, "value is not positive: {}".format(x)
        self._x = x

    def y(self, y):
        ''' set y with data validation '''
        assert isinstance(y, int), "value is not an integer: {}".format(y)
        assert y >= 0, "value is not positive: {}".format(y)
        self._y = y

    def __add__(self, value):
        return xy(self._x + value._x, self._y + value._y)

    def __sub__(self, value):
        return xy(self._x - value._x, self._y - value._y)

    def astuple(self):
        return (self._x, self._y)

    def __repr__(self):
        return "({},{})".format(self._x, self._y)

class rectangle():
    _DEFAULT_COLOR = "white"
    _DEFAULT_BORDER = "black"

    def __init__(self, origin, dimensions, color=None, border=False):
        ''' origin: coodinates of upper left pixel (xy object or tuple)
            dimensions: width and height (xy object or tuple) '''

        if isinstance(origin, tuple):
            self.orig = xy(origin[0], origin[1])
        else:
            self.orig = origin

        if isinstance(dimensions, tuple):
            self.dims = xy(dimensions[0], dimensions[1])
        else:
            self.dims = dimensions

        if color:
            self.color = color
        else:
            self.color = rectangle._DEFAULT_COLOR

        self._border = border
        if border:
            self._border_color = rectangle._DEFAULT_BORDER
        else:
            self._border_color = self.color

    def set_border(self, setting):
        self._border = setting

    def show(self):
        # Create an image to draw on. This will be handled by
        # tree object ultimately, I think
        img = Image.new("RGBA", (500, 500), "black")

        # Create a draw to draw on. This will stay in here,
        # I think
        draw = ImageDraw.Draw(img)

        top_left = self.orig.astuple()
        bottom_right = (self.orig + self.dims).astuple()

        if self._border:
            border = self._border_color
        else:
            border = self.color

        draw.rectangle([top_left, bottom_right], self.color, border)

        img.show()

    def __repr__(self):
        return "rectangle({}, {}, {}, {})".format(self.orig, self.dims, self.color, self._border)