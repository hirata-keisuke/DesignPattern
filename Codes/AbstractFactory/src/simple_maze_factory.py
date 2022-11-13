from .abstract_maze_factory import AbstractMazeFactory
from .maze  import Maze
from .abstract_site import MapSite

class SimpleMazeFactory(AbstractMazeFactory):

    def __init__(self):
        ...

    def make_maze(self):
        return Maze()

    def make_room(self, number):
        return self.SimpleRoom(number)

    def make_door(self, room1, room2):
        return self.SimpleDoor()
    
    def make_wall(self):
        return self.SimpleWall()

    class SimpleRoom(MapSite):

        def __init__(self, room_number):
            super().__init__()
            self._number = room_number
            self._west = None
            self._east = None
            self._north = None
            self._south = None

        @property
        def number(self):
            return self._number

        @number.setter
        def number(self, rooo_number):
            self._number = rooo_number

        @property
        def west(self):
            return self._west
        
        @property
        def east(self):
            return self._east
        
        @property
        def north(self):
            return self._north
        
        @property
        def south(self):
            return self._south

        @west.setter
        def west(self, neighbor):
            self._west = neighbor

        @east.setter
        def east(self, neighbor):
            self._east = neighbor

        @north.setter
        def north(self, neighbor):
            self._north = neighbor

        @south.setter
        def south(self, neighbor):
            self._south = neighbor

        def enter(self):
            return self

    class SimpleWall(MapSite):

        def __init__(self):
            super().__init__()

        def enter(self):
            return "引き返す"

    class SimpleDoor(MapSite):

        def __init__(self):
            super().__init__()

        def enter(self):
            return "次の部屋へ"