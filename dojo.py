from apps.person import Staff, Fellow
from apps.rooms import Office, LivingSpace
import random


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

        if role == "FELLOW":
            new_person = Fellow(person_name)
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
        elif role == "STAFF":
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
        else:
            print("You've entered an invalid role. Please choose either Fellow or Staff")

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
