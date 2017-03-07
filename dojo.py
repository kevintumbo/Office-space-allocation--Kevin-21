from apps.person import Staff, Fellow
from apps.rooms import Office, LivingSpace
import random


class Dojo(object):
    def __init__(self):
        self.total_rooms = []
        self.total_people = []
        self.available_offices = []
        self.available_living_space = []

    def create_room(self, room_type, room_name):

        """ creates a unique new room space """

        for room in room_name:
            if room in [room.room_name for room in self.total_rooms]:
                print('sorry that room name already exists')
            else:
                if room_type == "office":
                    new_office = Office(room)
                    self.total_rooms.append(new_office)
                    print('An office called {0} has been successfully created!'.format(new_office.room_name))

                elif room_type == "living":
                    new_living_space = LivingSpace(room)
                    self.total_rooms.append(new_living_space)
                    print('A living space called {0} has been successfully created!'.format(new_living_space.room_name))

    def add_person(self, first_name, last_name, role, accommodation="N"):

        """ adds a new person to the system """
        person_name = first_name + " " + last_name

        if role == "Fellow" or role == "Staff":
            self.check_availability()

            if not self.available_offices:
                print('sorry no offices available at the moment. please try again later')

            elif role == "Fellow":
                new_person = Fellow(person_name)
                self.total_people.append(new_person)
                self.allocate_office(new_person)
                if accommodation == 'Y':
                    if not self.available_living_space:
                        print('sorry no living space available at the moment. please try again later ')
                    else:
                        self.allocate_living_space(new_person)

            elif role == "Staff":
                new_person = Staff(person_name)
                self.total_people.append(new_person)
                self.allocate_office(new_person)
                if accommodation == 'Y':
                    print('Sorry living space is for fellows only')
        else:
            print("You've entered an invalid role. Please choose either Fellow or Staff")

    def check_availability(self):

        """ checks if rooms have vacant spaces"""

        if self.total_rooms:
            for room in self.total_rooms:

                if room.type == "office":
                    if len(room.occupants) >= room.maximum_occupants:
                        if room in self.available_offices:
                            self.available_offices.remove(room)
                    elif len(room.occupants) < room.maximum_occupants:
                        if room not in self.available_offices:
                            self.available_offices.append(room)

                elif room.type == "living":
                    if len(room.occupants) >= room.maximum_occupants:
                        if room in self.available_living_space:
                            self.available_living_space.remove(room)
                    elif len(room.occupants) < room.maximum_occupants:
                        if room not in self.available_living_space:
                            self.available_living_space.append(room)

    def allocate_office(self, new_person):

        """ Allocates vacant office space to person"""

        office = random.choice(self.available_offices)
        office.occupants.append(new_person)
        print('{0} has been allocated the office {1}'.format(new_person.person_name, office.room_name))

    def allocate_living_space(self, new_person):

        """ Allocates vacant living space to person"""

        living_space = random.choice(self.available_living_space)
        living_space.occupants.append(new_person)
        print('{0} has been allocated the living spaces {1}'.format(new_person.person_name, living_space.room_name))
