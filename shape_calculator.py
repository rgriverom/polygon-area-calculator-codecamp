"""Arithmetic Formatter"""


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape: 'Rectangle' or 'Square'):
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side: int):
        super().set_width(side)
        super().set_height(side)

    def get_area(self):
        return super().get_area()

    def get_perimeter(self):
        return super().get_perimeter()

    def get_diagonal(self):
        return super().get_diagonal()

    def get_picture(self):
        return super().get_picture()

    def get_amount_inside(self, shape: 'Rectangle' or 'Square'):
        return super().get_amount_inside(shape)
