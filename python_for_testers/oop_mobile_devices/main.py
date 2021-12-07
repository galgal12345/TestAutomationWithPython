from python_for_testers.oop_mobile_devices.MobileDevice import MobileDevices

device2 = MobileDevices("A6000", "Android", 11, False, 1800, 2280, 1080)
MobileDevices.print_parameters(device2.model, device2.os, device2.version, device2.has_flash, device2.price)
print(MobileDevices.calculate_area(device2.screen_width, device2.screen_height))
MobileDevices.picture_quality(device2.has_flash)

device2 = MobileDevices("B5000", "IOS", 8, True, 3600, 3350, 2200)
MobileDevices.print_parameters(device2.model, device2.os, device2.version, device2.has_flash, device2.price)
print(MobileDevices.calculate_area(device2.screen_width, device2.screen_height))
MobileDevices.picture_quality(device2.has_flash)
