"""
Remove unnecessary interface elements from parent class.
"""


class CPU:
    def compute(self) -> None:
        print("computing")


class GFX:
    def render_video(self) -> None:
        print("Rendering video...")


class Mobo:
    def enable_cooler(self) -> None:
        print * ("Enabling cooler...")


class PSU:
    def supply_power(self) -> None:
        print("Supplying power...")


class Ports:
    def usb2(self) -> str:
        ...

    def usb3(self) -> str:
        ...

    def thunderbolt(self) -> str:
        ...


class PC(Ports, GFX, CPU, Mobo, PSU):
    def usb3(self) -> str:
        return "USB-C"

    def mini_jack(self) -> str:
        return "Mini Jack"


class Mac(Ports, GFX, CPU, Mobo, PSU):
    def usb3(self) -> str:
        return "USB-C"

    def thunderbolt(self) -> str:
        return "Thunderbolt"
