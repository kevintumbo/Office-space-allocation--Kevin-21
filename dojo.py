from apps.person import Staff, Fellow
from apps.rooms import Office, LivingSpace
from apps.database import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import random
import os


class Dojo(object):
    def __init__(self):
        self.total_rooms = []
        self.total_people = []
        self.available_offices = []
        self.available_living_space = []
        self.waiting_for_office_allocation = []
        self.waiting_for_living_space_allocation = []

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
        if person_name in [person.person_name for person in self.total_people]:
            return "That Name is already in the system. Please enter different name or use middle name"

        if role != "FELLOW" and role != "STAFF":
            return "You've entered an invalid role. Please choose either FELLOW or STAFF"

        else:
            if role == "FELLOW":
                new_person = Fellow(person_name, accommodation)
                self.total_people.append(new_person)
                self.check_availability()
                if self.available_offices:
                    self.allocate_room(new_person, room="office")
                else:
                    self.waiting_for_office_allocation.append(new_person)
                    print('sorry no offices available at the moment. please try again later')
                if accommodation == 'Y':
                    if not self.available_living_space:
                        self.waiting_for_living_space_allocation.append(new_person)
                        print('sorry no living space available at the moment. please try again later ')
                    else:
                        self.allocate_room(new_person, room="living")
            if role == "STAFF":
                new_person = Staff(person_name)
                self.total_people.append(new_person)
                self.check_availability()
                if self.available_offices:
                    self.allocate_room(new_person, room="office")
                else:
                    self.waiting_for_office_allocation.append(new_person)
                    print('sorry no offices available at the moment. please try again later')
                if accommodation == 'Y':
                    print('Sorry living space is for fellows only')

    def check_availability(self):

        """ checks if rooms have vacant spaces"""

        if self.total_rooms:
            for room in self.total_rooms:
                if room.type == "office":
                    if len(room.occupants) == room.maximum_occupants:
                        if room in self.available_offices:
                            self.available_offices.remove(room)
                    elif len(room.occupants) < room.maximum_occupants:
                        if room not in self.available_offices:
                            self.available_offices.append(room)
                elif room.type == "living":
                    if len(room.occupants) == room.maximum_occupants:
                        if room in self.available_living_space:
                            self.available_living_space.remove(room)
                    elif len(room.occupants) < room.maximum_occupants:
                        if room not in self.available_living_space:
                            self.available_living_space.append(room)

    def allocate_room(self, new_person, room):

        """ Allocates vacant office  or living space to person"""
        if room == "office":
            office = random.choice(self.available_offices)
            office.occupants.append(new_person)
            print('{0} has been allocated the office {1}'.format(new_person.person_name, office.room_name))

        else:
            living_space = random.choice(self.available_living_space)
            living_space.occupants.append(new_person)
            print('{0} has been allocated the living spaces {1}'.format(new_person.person_name, living_space.room_name))

    def print_room(self, room):
        """ checks if room name given exists in the list of total rooms.
            if so it prints out a statement that highlights the room name,
            the room type and occupants.
        """
        if room not in [room.room_name for room in self.total_rooms]:
            print("Sorry.That rooms does not exist.")
        else:
            for room_to_check in self.total_rooms:
                if room == room_to_check.room_name:
                    if len(room_to_check.occupants) > 0:
                        people = []
                        for occupant in room_to_check.occupants:
                            people.append(occupant.person_name)
                        str1 = ', '.join(str(e) for e in people)
                        print("{0} space {1} contains {2}".format(room_to_check.type, room_to_check.room_name, str1))
                    else:
                        print("{0} space {1} contains no occupants".format(room_to_check.type, room_to_check.room_name))

    def print_allocations(self, filename=None):
        """
        this method checks if a room exists and if the room has occupants.
        if so it prints out a statement highlighting the room name and the names of its occupants
        """
        if not self.total_rooms:
            print("Sorry.No rooms exist. Please create one")
        else:
            for room in self.total_rooms:
                if len(room.occupants) > 0:
                    people = []
                    for occupant in room.occupants:
                        people.append(occupant.person_name)
                    str1 = ', '.join(str(e) for e in people)
                    if filename:
                        file = open(filename + ".txt", "a")
                        file.write("\n" + "{} \n".format(room.room_name))
                        file.write("\n" + "------------------------------------------\n")
                        file.write("\n" + "{}".format(str1) + "\n")
                        file.close()

                    print("\n"
                          "{} \n".format(room.room_name),
                          "\n"
                          "------------------------------------------"
                          "\n"
                          "{0}".format(str1),
                          "\n"
                          )
                else:
                    if filename:
                        file = open(filename + ".txt", "a")
                        file.write("\n" + "{} \n".format(room.room_name))
                        file.write("\n" + "------------------------------------------\n")
                        file.write("This {} space contains no occupants".format(room.type) + "\n")
                        file.close()

                    print("\n"
                          "{} \n".format(room.room_name),
                          "\n"
                          "------------------------------------------\n"
                          "\n"
                          "This {} space contains no occupants".format(room.type),
                          "\n"
                          )

    def print_unallocated(self, filename=None):
        """
        this method checks if there are people in the dojo who are unallocated rooms
        either because a certain type of room doesn't exist or the room requested is full.
        it prints out a statement highlighting the people who lack rooms and the type of room
        they lack.
        """

        if len(self.waiting_for_office_allocation) == 0 and len(self.waiting_for_living_space_allocation) == 0:
            print("There are no people who lack Rooms")

        if len(self.waiting_for_office_allocation) > 0:
            people = []
            for person in self.waiting_for_office_allocation:
                people.append(person.person_name)
            str1 = ', '.join(str(e) for e in people)

            print("\n"
                  "people who lack offices \n",
                  "\n"
                  "------------------------------------------\n"
                  "\n"
                  "{}".format(str1),
                  "\n"
                  )

            if filename:
                print("printing file...")
                file = open(filename + ".txt", "a")
                file.write("\n" + "people who lack offices \n")
                file.write("\n" + "------------------------------------------\n")
                file.write("{}".format(str1) + "\n")
                file.close()

        if len(self.waiting_for_living_space_allocation) > 0:
            people = []
            for person in self.waiting_for_living_space_allocation:
                people.append(person.person_name)
            str1 = ', '.join(str(e) for e in people)

            print("\n"
                  "people who lack Living spaces \n",
                  "\n"
                  "------------------------------------------\n"
                  "\n"
                  "{}".format(str1),
                  "\n"
                  )

            if filename:
                print("printing file...")
                file = open(filename + ".txt", "a")
                file.write("\n" + "people who lack Living spaces \n")
                file.write("\n" + "------------------------------------------\n")
                file.write("{}".format(str1) + "\n")
                file.close()

    def reallocate_person(self, first_name, last_name, new_room_name):
        person_identifier = first_name + " " + last_name

        if person_identifier not in [person.person_name for person in self.total_people]:
            return "Sorry that person does not exist"

        if new_room_name not in [room.room_name for room in self.total_rooms]:
            return "Sorry that room does not exist"

        for person in self.total_people:
            if person_identifier == person.person_name:
                person_reallocating = person

        rooms_occupied = []

        for room in self.total_rooms:
            if room.room_name == new_room_name:
                room_to_relocate = room
            if person_reallocating in room.occupants:
                rooms_occupied.append(room)

        if len(room_to_relocate.occupants) == room_to_relocate.maximum_occupants:
            return "sorry that room is full"

        else:
            if room_to_relocate.type == "office":
                if person_reallocating in self.waiting_for_office_allocation:
                    self.waiting_for_office_allocation.remove(person_reallocating)
                    room_to_relocate.occupants.append(person_reallocating)
                    return "{0} has been successfully allocated {1} {2}" \
                        .format(person_reallocating.person_name, room_to_relocate.type, room_to_relocate.room_name)
                else:
                    for room_occupied in rooms_occupied:
                        if room_occupied.room_name == room_to_relocate.room_name:
                            return "sorry. you cannot reallocate to the same room"
                        if room_occupied.type == room_to_relocate.type:
                            room_occupied.occupants.remove(person_reallocating)
                            room_to_relocate.occupants.append(person_reallocating)
                            return "{0} have successfully been reallocated from {1} to {2}." \
                                .format(person_reallocating.person_name, room_occupied.room_name,
                                        room_to_relocate.room_name)

            if room_to_relocate.type == "living":
                if person_reallocating.role == "STAFF":
                    return "Sorry.staff cannot be allowed in living space"
                if person_reallocating in self.waiting_for_living_space_allocation:
                    self.waiting_for_living_space_allocation.remove(person_reallocating)
                    room_to_relocate.occupants.append(person_reallocating)
                    return "{0} has been successfully allocated {1} {2}" \
                        .format(person_reallocating.person_name, room_to_relocate.type, room_to_relocate.room_name)
                else:
                    for room_occupied in rooms_occupied:
                        if room_occupied.room_name == room_to_relocate.room_name:
                            return "sorry. you cannot reallocate to the same room"
                        if room_occupied.type == room_to_relocate.type:
                            room_occupied.occupants.remove(person_reallocating)
                            room_to_relocate.occupants.append(person_reallocating)
                            return "{0} have successfully been reallocated from {1} to {2}." \
                                .format(person_reallocating.person_name, room_occupied.room_name,
                                        room_to_relocate.room_name)

    def load_people(self, filename):
        if os.path.isfile(filename + ".txt"):
            file = open(filename + ".txt").readlines()
            for person in file:
                string = person.split()
                first_name = string[0]
                last_name = string[1]
                role = string[2]
                if len(string) > 3:
                    accommodation = string[3]
                else:
                    accommodation = "N"
                self.add_person(first_name, last_name, role, accommodation)
        else:
            return "Sorry that file does not exist"

    def save_state(self, db_name=None):
        """ This method saves data from app into database"""

        if db_name:
            db = db_name + '.db'
            engine = create_engine('sqlite:///{}'.format(db))
        else:
            engine = create_engine('sqlite:///dojo.db')

        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        new_session = session()

        # loop through all rooms
        for space in self.total_rooms:
            room = Room()

            room.room_name = space.room_name
            room.room_type = space.type
            room.maximum_occupants = space.maximum_occupants
            room.current_occupants = len(space.occupants)

            new_session.add(room)
            new_session.commit()

        # loop through all people
        for individual in self.total_people:
            person = People()

            person.name = individual.person_name
            person.role = individual.role
            person.accomodation = individual.accomodation

            for space in self.total_rooms:
                if individual in space.occupants and space.type == "office":
                    person.office_allocated = space.room_name
                if individual in space.occupants and space.type == "living":
                    person.living_space_allocated = space.room_name

            new_session.add(person)
            new_session.commit()

        return 'You have saved data to the database'

    def load_state(self, db_name=None):
        """ Loads data from database into from app """
        if os.path.isfile(db_name + ".db"):

            if db_name:
                db = db_name + '.db'
                engine = create_engine('sqlite:///{}'.format(db))
            else:
                engine = create_engine('sqlite:///dojo.db')

            session = sessionmaker(bind=engine)
            new_session = session()

            people = new_session.query(People).all()
            rooms = new_session.query(Room).all()

            for room in rooms:
                room_name = room.room_name
                room_type = room.room_type

                if room_type == "office":
                    load_office = Office(room_name)
                    self.total_rooms.append(load_office)

                if room_type == "living":
                    load_living_space = LivingSpace(room_name)
                    self.total_rooms.append(load_living_space)

            for person in people:
                person_name = person.name
                person_role = person.role
                person_accomodation = person.accomodation
                office_allocated = person.office_allocated
                living_space_allocated = person.living_space_allocated

                if person_role == "FELLOW":
                    load_person = Fellow(person_name, person_accomodation)
                    self.total_people.append(load_person)

                    if not office_allocated:
                        self.waiting_for_office_allocation.append(load_person)

                    if not living_space_allocated and person_accomodation == "Y":
                        self.waiting_for_living_space_allocation.append(load_person)

                    if office_allocated:
                        for room in self.total_rooms:
                            if room.room_name == office_allocated:
                                room.occupants.append(load_person)

                    if living_space_allocated:
                        for room in self.total_rooms:
                            if room.room_name == living_space_allocated:
                                room.occupants.append(load_person)

                if person_role == "STAFF":
                    load_person = Staff(person_name)
                    self.total_people.append(load_person)

                    if not office_allocated:
                        self.waiting_for_office_allocation.append(load_person)

                    if office_allocated:
                        for room in self.total_rooms:
                            if room.room_name == office_allocated:
                                room.occupants.append(load_person)

            return 'database has been loaded'
        else:
            return 'Sorry that database file cannot be found'
