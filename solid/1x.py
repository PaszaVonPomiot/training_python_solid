"""
Incorporate variables and functions into available classes.
Make best effort to follow Single Responsibility Principle.
"""


# attributes
inventory = ["bread", "cola", "bleach"]
age = 38
file_name = "report"
ammo = 17
height = 178
compression = True
price = 1200.50


# methods
def generate_pdf():
    ...


def generate_xlsx():
    ...


def drink():
    ...


def eat():
    ...


def shoot():
    ...


def reload():
    ...


# classes
class Exporter:
    ...


class Person:
    ...


class Weapon:
    ...
