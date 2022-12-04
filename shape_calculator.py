class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""

        for i in range(self.height):
            for j in range(self.width):
                picture += "*"
            picture += "\n"

        return picture

    def get_amount_inside(self, other) -> int:

        amount = 0

        area = self.get_area()

        while area >= other.get_area():
            area -= other.get_area()
            amount += 1

        return amount

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.set_side(side)

    def set_side(self, side) -> None:
        super().set_height(side)
        super().set_width(side)

    def set_height(self, height: int) -> None:
        self.set_side(height)

    def set_width(self, width: int) -> None:
        self.set_side(width)

    def __str__(self) -> str:
        return f"Square(side={self.height})"
