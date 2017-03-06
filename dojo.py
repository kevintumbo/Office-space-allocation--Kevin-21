from apps.person import Staff, Fellow
from apps.rooms import Office, LivingSpace
import random


class Dojo(object):
    def __init__(self):
        self.total_rooms = []
        self.offices = []
        self.living_spaces = []
        self.total_people = []
        self.available_offices = []
        self.available_living_space = []
        self.staff = []
        self.fellows = []

    def create_room(self, room_type, room_name):
        if [office for office in room_name if office in self.total_rooms]:
            print('sorry that room name already exists')
        else:
            if room_type == "office":
                for rm in room_name:
                    new_office = Office(rm)
                    self.offices.append(new_office)
                    self.total_rooms.append(new_office.room_name)
                    print('An office called {0} has been successfully created!'.format(new_office.room_name))

            elif room_type == "living":
                for rm in room_name:
                    new_living_space = LivingSpace(rm)
                    self.living_spaces.append(new_living_space)
                    self.total_rooms.append(new_living_space.room_name)
                    print('A living space called {0} has been successfully created!'.format(new_living_space.room_name))

    def add_person(self, person_name, role, accommodation):
        if role == "Fellow" or role == "Staff":
            self.check_office_space_available()
            self.check_living_space_available()

            if not self.available_offices:
                print('sorry no offices available at the moment. please try again later')

            elif role == "Fellow":
                new_person = Fellow(person_name)
                self.total_people.append(new_person)
                self.fellows.append(new_person)
                self.allocate_office(new_person)
                if accommodation == 'Y':
                    if not self.available_living_space:
                        print('sorry no living space available at the moment. please try again later ')
                    else:
                        self.allocate_living_space(new_person)

            elif role == "Staff":
                new_person = Staff(person_name)
                self.total_people.append(new_person)
                self.staff.append(new_person)
                self.allocate_office(new_person)
                if accommodation == 'Y':
                    print('Sorry living space is for fellows only')
        else:
            print("You've entered an invalid role. Please choose either Fellow or Staff")

    def allocate_office(self, new_person):
        office = random.choice(self.available_offices)
        office.occupants.append(new_person)
        print('{0} has been allocated the office {1}'.format(new_person.person_name, office.room_name))

    def allocate_living_space(self, new_person):
        living_space = random.choice(self.available_living_space)
        living_space.occupants.append(new_person)
        print('{0} has been allocated the living spaces {1}'.format(new_person.person_name, living_space.room_name))

    def check_office_space_available(self):
        if self.offices:
            for office in self.offices:
                if len(office.occupants) >= office.max:
                    if office in self.available_offices:
                        self.available_offices.remove(office)
                elif len(office.occupants) < office.max:
                    if office not in self.available_offices:
                        self.available_offices.append(office)

    def check_living_space_available(self):
        if self.living_spaces:
            for space in self.living_spaces:
                if len(space.occupants) >= space.max:
                    if space in self.available_living_space:
                        self.available_living_space.remove(space)
                elif len(space.occupants) < space.max:
                    if space not in self.available_living_space:
                        self.available_living_space.append(space)
