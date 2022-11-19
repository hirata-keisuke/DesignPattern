from abc import ABC, abstractmethod

class PrototypeMapsite(ABC):

    @abstractmethod
    def clone(self):
        ...

class Door(ABC):

    def __init__(self, r1, r2):
        self._room1 = r1
        self._room2 = r2

    @abstractmethod
    def effect(self):
        ...

class SimpleDoor(PrototypeMapsite, Door):

    def clone(self):
        return SimpleDoor(self._room1, self._room2)

    def effect(self):
        return "ただのドアです。"