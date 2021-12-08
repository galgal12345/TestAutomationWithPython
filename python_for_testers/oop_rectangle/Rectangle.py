from python_for_testers.oop_rectangle.Triangle import Triangle


class Rectangle(Triangle):

    def __init__(self, height, width):
        super().__init__(height, width)

    def calculate_area(self):
        return self.height * self.width
