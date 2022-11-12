class Room:

    def __init__(self, room_number):
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