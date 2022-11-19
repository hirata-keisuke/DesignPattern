from abc import ABC, abstractmethod

class PrototypeMapsite(ABC):

    @abstractmethod
    def clone(self):
        ...

    @abstractmethod
    def effect(self):
        ...

class Door(ABC):

    def __init__(self, r1, r2):
        self._room1 = r1
        self._room2 = r2

class Room(ABC):

    def __init__(self, number):
        self._number = number
        self._east = None
        self._west = None
        self._south = None
        self._north = None    

class SimpleDoor(PrototypeMapsite, Door):

    def clone(self):
        return SimpleDoor(self._room1, self._room2)

    def effect(self):
        return "ただのドアです。"

class SimpleRoom(PrototypeMapsite, Room):

    def clone(self):
        return SimpleRoom(self._number)

    def effect(self):
        return "ただの部屋です。"