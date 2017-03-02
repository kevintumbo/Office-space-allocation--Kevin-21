class Dojo(object):
    def __init__(self):
        self.total_rooms = []
        self.offices = []
        self.living_spaces = []
        self.total_people = []
        self.staff = []
        self.fellows = []

    def create_room(self, room_type, room_name):
        pass

    def add_person(self, person_name, role, accommodation='No'):
        pass

    def __del__(self):
        print("Destructor started")
