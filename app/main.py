from __future__ import annotations
from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str) -> None:
        self.health: int = 100
        self.name: str = name
        self.hidden: bool = False
        Animal.alive.append(self)

    def die(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            "{Name: "
            f"{self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            "}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            herbivore.die()
