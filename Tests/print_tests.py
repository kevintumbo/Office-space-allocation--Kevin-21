import unittest
from dojo import Dojo


class TestPrintCreation(unittest.TestCase):

    """ Test cases to for successful and failed  printing of lists"""

    def test_can_print_names_of_people_in_room(self):

        """ test successful printing of names of people in room_name on screen"""

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Kevin', 'Oriels', 'Fellow')
        print_room = self.dojo.print_room("kenya")
        self.assertEquals(print_room, "Kenya Contains Kevin Oriels")

    def test_successful_print_list_of_allocation(self):

        """ test successful printing of names of people allocated a room on screen"""
        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Kevin', 'Oriels', 'Fellow')
        self.dojo.add_person('John', 'john', 'Staff')
        self.dojo.add_person('Anne', 'Ndinda', 'Fellow')
        print_allocation = self.dojo.print_allocations()
        self.assertEquals(print_allocation, "Kenya : Kevin Oriels, John john, Anne Ndinda")

    def test_successful_print_list_of_unallocated(self):

        """ test successful printing of names of people not allocated a room on screen"""
        self.dojo = Dojo()
        self.dojo.add_person('Diego', 'Pamio', 'Fellow')
        self.dojo.add_person('Brad', 'Pitcher', 'Staff')
        print_allocation = self.dojo.print_unallocated()
        self.assertEquals(print_allocation, "Unallocated: Diego Pamio, Brad Pitcher")

    def test_cannot_print_list_for_room_not_existing(self):

        """ test unsuccessful printing of names of people in room_name that does not exist """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        print_room = self.dojo.print_room("Britain")
        self.assertEquals(print_room, "Sorry. No such room Exists")

    def test_can_print_empty_room(self):

        """ test  printing of names of people in room_name that does not exist """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        print_room = self.dojo.print_room("kenya")
        self.assertEquals(print_room, "Kenya is currently empty")
