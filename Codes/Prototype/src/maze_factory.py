from abc import ABC, abstractmethod

class MazeFactory(ABC):

    @abstractmethod
    def make_wall(self):
        ...

    @abstractmethod
    def make_room(self, num):
        ...

    @abstractmethod
    def make_door(self, r1, r2):
        ...

class MazePrototypeFactory(MazeFactory):

    def __init__(self, m, w, r, d):
        self._prototypeMaze = m
        self._prototypeWall = w
        self._prototypeRoom = r
        self._prototypeDoor = d

    def make_wall(self):
        return self._prototypeWall.clone()

    def make_room(self, num):
        return self._prototypeRoom.clone(num)

    def make_door(self, r1, r2):
        door = self._prototypeDoor.clone()
        door.intialize(r1, r2)
        return door