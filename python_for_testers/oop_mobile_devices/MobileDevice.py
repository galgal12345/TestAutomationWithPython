class MobileDevices:
    model = ""
    os = ""
    version = 0
    has_flash = None
    price = 0
    screen_width = 0
    screen_height = 0

    def __init__(self, model, os, version, has_flash, price, width, height):
        self.model = model
        self.os = os
        self.version = version
        self.has_flash = has_flash
        self.price = price
        if height > 0 and width > 0:
            self.screen_width = width
            self.screen_height = height

    def print_parameters(price, has_flash, version, os, model):
        print(model)
        print(os)
        print(version)
        print(has_flash)
        print(price)

    def calculate_area(screen_width, screen_height):
        return screen_height * screen_width

    def picture_quality(self):
        if self:
            print("Good Quality")
        else:
            print("Bad Quality")
        print()
