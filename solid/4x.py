"""
Remove unnecessary interface elements from parent class.
"""


class CPU:
    ...


class GFX:
    ...


class Mobo:
    ...


class PSU:
    ...


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
