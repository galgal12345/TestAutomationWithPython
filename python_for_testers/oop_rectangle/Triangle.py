class Triangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return (self.height * self.width) / 2
