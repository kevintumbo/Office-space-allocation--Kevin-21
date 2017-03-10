import unittest
import os
from dojo import Dojo


class TestPrintCreation(unittest.TestCase):

    """ Test cases to for successful and failed  printing of lists"""

    def test_can_print_names_of_people_in_room_on_screen(self):

        """ test successful printing of names of people in room_name on screen"""

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Kevin', 'Oriels', 'Fellow')
        print_room = self.dojo.print_room("kenya")
        self.assertTrue(print_room, "Kenya Contains Kevin Oriels")

    def test_successful_print_list_of_allocation_on_screen(self):

        """ test successful printing of names of people allocated a room on screen"""
        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Kevin', 'Oriels', 'Fellow')
        print_allocation = self.dojo.print_allocations()
        self.assertEquals(print_allocation, "Kenya : Kevin Oriels")

    def test_successful_print_list_of_unallocated_on_screen(self):

        """ test successful printing of names of people not allocated a room on screen"""
        self.dojo = Dojo()
        self.dojo.add_person('Diego', 'Pamio', 'Fellow')
        print_allocation = self.dojo.print_unallocated()
        self.assertEquals(print_allocation, "Unallocated: Diego Pamio")

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

    def test_successful_print_list_of_allocation_to_txt_file(self):

        """ test successful printing of names of people allocated a room to a txt file """
        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Kevin', 'Oriels', 'Fellow')
        self.dojo.print_allocations("allocated_persons")
        self.assertTrue(os.path.isfile("allocated_persons.txt"))
        with open("allocated_persons.txt", "r") as allocated_file:
            first_line = allocated_file[0]
            third_line = allocated_file[2]
            self.assertEquals(first_line, "kenya")
            self.assertEquals(third_line, "Kevin Oriels")
        os.remove("allocated_persons.txt")

    def test_successful_print_list_of_unallocated_to_txt_file(self):

        """ test successful printing of names of people not allocated a room to a txt file """
        self.dojo = Dojo()
        self.dojo.add_person('Diego', 'Pamio', 'Fellow')
        self.dojo.print_unallocated("unallocated_persons")
        self.assertTrue(os.path.isfile("unallocated_persons.txt"))
        with open("unallocated_persons.txt", "r") as unallocated_file:
            first_line = unallocated_file.readline().strip()
            self.assertEquals(first_line, "Diego Pamio awaiting office")
        os.remove("unallocated_persons.txt")

