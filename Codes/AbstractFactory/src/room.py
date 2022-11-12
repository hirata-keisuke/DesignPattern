class Room:

    def __init__(self, room_number):
        self._number = room_number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, rooo_number):
        self._number = rooo_number