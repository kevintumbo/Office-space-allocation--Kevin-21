class Room(object):
    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = []


class Office(Room):
    def __init__(self, room_name):
        super().__init__(room_name)

        self.max = 6


class LivingSpace(Room):
    def __init__(self, room_name):
        super().__init__(room_name)

        self.max = 4

