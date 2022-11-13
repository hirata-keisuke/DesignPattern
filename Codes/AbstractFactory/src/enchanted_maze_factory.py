from .abstract_maze_factory import AbstractMazeFactory
from .maze  import Maze
from .abstract_site import MapSite
    
class EnchantedMazeFactory(AbstractMazeFactory):

    def __init__(self):
        ...

    def make_maze(self):
        return Maze()

    def make_room(self, number):
        return self.EnchantedRoom(number, self.Spell())

    def make_door(self, room1, room2):
        return self.EnchantedDoor(self.Spell())
    
    def make_wall(self):
        return self.EnchantedWall(self.Spell())

    class EnchantedRoom(MapSite):

        def __init__(self, room_number, spell):
            super().__init__()
            self._number = room_number
            self.spell = spell
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

    class EnchantedWall(MapSite):

        def __init__(self, spell):
            super().__init__()
            self.spell = spell

        def enter(self):
            return "引き返す"

    class EnchantedDoor(MapSite):

        def __init__(self, spell):
            super().__init__()
            self.spell = spell

        def enter(self, spell):
            if spell == self.spell:
                return "次の部屋へ"
            else:
                return "引き返す"

    class Spell:
        def __init__(self):
            self.spell = "開けゴマ"
        