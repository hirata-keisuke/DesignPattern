class Maze:

    def __init__(self):
        self.rooms = {}
        
    def add_room(self, name, room):
        self.rooms[name] = room