"""
Find and fix LSP violation
"""

from abc import ABC, abstractmethod


from enum import Enum


class ViolenceEnum(int, Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    BLOODY = 4


class Game(ABC):
    def __init__(self, name: str, multiplayer: bool, violence: ViolenceEnum) -> None:
        self.name = name
        self.multiplayer = multiplayer
        self.violence = violence
        self.slot = 2
        self.score = 0

    def start(self) -> None:
        print(f"Starting {self.name}")

    @abstractmethod
    def get_highscore(self) -> float:
        ...

    def save(self) -> None:
        print(f"Saving to slot {self.slot}")


class Dota(Game):
    def get_highscore(self) -> int:
        return self.score


dota = Dota(
    name="Defense of the Ancients", multiplayer=True, violence=ViolenceEnum.BLOODY
)
dota.score = 1000
print(dota.get_highscore())
