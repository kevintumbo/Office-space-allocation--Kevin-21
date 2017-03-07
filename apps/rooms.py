class Room(object):

    """ class Room """

    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = []


class Office(Room):

    """ class office inheriting from parent class room"""

    def __init__(self, room_name):
        super().__init__(room_name)

        self.maximum_occupants = 6
        self.type = "office"


class LivingSpace(Room):

    """ class LivingSpace inheriting from parent class room"""

    def __init__(self, room_name):
        super().__init__(room_name)

        self.maximum_occupants = 4
        self.type = "living"
