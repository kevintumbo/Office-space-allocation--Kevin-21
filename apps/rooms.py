class Room(object):

    """ class Room """

    def __init__(self, room_name, maximum_occupants=None, type=None):
        self.room_name = room_name
        self.occupants = []
        self.maximum_occupants = maximum_occupants
        self.type = type


class Office(Room):

    """ class office inheriting from parent class room"""

    def __init__(self, room_name):
        super().__init__(room_name, maximum_occupants=6, type="office")


class LivingSpace(Room):

    """ class LivingSpace inheriting from parent class room"""

    def __init__(self, room_name):
        super().__init__(room_name, maximum_occupants=4, type="living")

