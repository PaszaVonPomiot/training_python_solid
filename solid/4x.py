"""
Remove unnecessary interface elements from parent class.
"""

from abc import ABC, abstractmethod


class CPU:
    def compute(self) -> str:
        return "Computing..."


class GFX:
    def render_video(self) -> str:
        return "Rendering video..."


class Mobo:
    def enable_cooler(self) -> str:
        return "Enabling cooler..."


class PSU:
    def supply_power(self) -> str:
        return "Supplying power..."


class Ports(ABC):
    @abstractmethod
    def usb2(self) -> str:
        ...

    @abstractmethod
    def usb3(self) -> str:
        ...

    @abstractmethod
    def thunderbolt(self) -> str:
        ...


class Pc(Ports, GFX, CPU, Mobo, PSU):
    def usb3(self) -> str:
        return "USB-C"

    def mini_jack(self) -> str:
        return "Mini Jack"


class Mac(Ports, GFX, CPU, Mobo, PSU):
    def usb3(self) -> str:
        return "USB-C"

    def thunderbolt(self) -> str:
        return "Thunderbolt"
