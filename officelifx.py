import sys
from time import sleep
from lifxlan import LifxLAN

class Colors:
    RED = [65535, 65535, 65535, 3500]
    ORANGE = [6500, 65535, 65535, 3500]
    YELLOW = [9000, 65535, 65535, 3500]
    GREEN = [16173, 65535, 65535, 3500]
    CYAN = [29814, 65535, 65535, 3500]
    BLUE = [43634, 65535, 65535, 3500]
    PURPLE = [50486, 65535, 65535, 3500]
    PINK = [58275, 65535, 47142, 3500]
    WHITE = [58275, 0, 65535, 5500]
    COLD_WHITE = [58275, 0, 65535, 9000]
    WARM_WHITE = [58275, 0, 65535, 3200]
    GOLD = [58275, 0, 65535, 2500]
    AQUA = [26000, 65535, 65535, 3500]
    PEACH = [62000, 50000, 25000, 3200]

    def from_string(colorname):
        switcher={
            "red":Colors.RED,
            "orange":Colors.ORANGE,
            "yellow":Colors.YELLOW,
            "green":Colors.GREEN,
            "cyan":Colors.CYAN,
            "blue":Colors.BLUE,
            "purple":Colors.PURPLE,
            "pink":Colors.PINK,
            "white":Colors.WHITE,
            "coldwhite":Colors.COLD_WHITE,
            "warmwhite":Colors.WARM_WHITE,
            "gold":Colors.GOLD,
            "aqua":Colors.AQUA,
            "peach":Colors.PEACH
        }
        return switcher.get(colorname,"Invalid color")
    from_string = staticmethod(from_string)

class BuildLight:
    def __init__(self):
        lifx = LifxLAN()
        devices = lifx.get_color_lights()
        if len(devices) < 1:
            print('not found...')
            sleep(0.2)
            devices = lifx.get_color_lights()

        self.light = devices[0]

    def on(self):
        self.light.set_power(65535)
        self.light.set_brightness(65535)

    def off(self):
        self.light.set_power(0)
        self.light.set_brightness(0)

    def half(self):
        self.light.set_power(65535)
        self.light.set_brightness(32767)

    def set_color(self, color, duration=0, rapid=False):
        self.light.set_color(color, duration, rapid)

class CeilingLights:
    def __init__(self):
        lifx = LifxLAN()
        devices = lifx.get_color_all_lights()
        if len(devices) < 1:
            print('not found...')
            sleep(0.1)
            devices = lifx.get_color_all_lights()

        self.lights = []
        for l in devices:
            if not l.supports_color():
                self.lights.append(l)

    def on(self):
        for l in self.lights:
            l.set_power(1)
            l.set_brightness(65535)

    def off(self):
        for l in self.lights:
            l.set_power(0)
            l.set_brightness(0)

    def day(self):
        for l in self.lights:
            l.set_brightness(65535)
            l.set_colortemp(5600)
    
    def night(self):
        for l in self.lights:
            l.set_brightness(50000)
            l.set_colortemp(2700)