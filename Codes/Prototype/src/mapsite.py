from abc import ABC, abstractmethod

class PrototypeDoor(ABC):

    def __init__(self, r1, r2):
        self._room1 = r1
        self._room2 = r2

    @abstractmethod
    def effect(self):
        ...

class SimpleDoor(PrototypeDoor):

    def effect(self):
        return "ただのドアです。"