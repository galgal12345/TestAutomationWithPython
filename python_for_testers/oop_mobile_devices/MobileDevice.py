class MobileDevices:

    def __init__(self, model, os, version, has_flash, price, width, height):
        self.model = model
        self.os = os
        self.version = version
        self.has_flash = has_flash
        self.price = price

        if height > 0 and width > 0:
            self.screen_width = width
            self.screen_height = height

    def print_parameters(self):
        print(self.model)
        print(self.os)
        print(self.version)
        print(self.has_flash)
        print(self.price)

    def calculate_area(self):
        return self.screen_height * self.screen_width

    def picture_quality(self):
        if self:
            print("Good Quality")
        else:
            print("Bad Quality")
        print()
