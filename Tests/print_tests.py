import unittest
import os
import sys
from dojo import Dojo


class TestPrintCreation(unittest.TestCase):

    """ Test cases to for successful and failed  printing of lists"""

    def test_can_print_names_of_people_in_room_on_screen(self):

        """ test successful printing of names of people in room_name on screen"""

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Kevin', 'Oriels', 'FELLOW')
        self.dojo.print_room("kenya")
        saved = sys.stdout
        output =saved.getvalue()
        self.assertIn("office space kenya contains Kevin Oriels", output)

    def test_successful_print_list_of_allocation_on_screen(self):

        """ test successful printing of names of people allocated a room on screen"""
        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Kevin', 'Oriels', 'FELLOW')
        self.dojo.print_allocations()
        saved = sys.stdout
        output =saved.getvalue()
        self.assertIn('Kevin Oriels' , output)

    def test_successful_print_list_of_unallocated_on_screen(self):

        """ test successful printing of names of people not allocated a room on screen"""
        self.dojo = Dojo()
        self.dojo.add_person('Diego', 'Pamio', 'FELLOW')
        self.dojo.print_unallocated()
        saved = sys.stdout
        output =saved.getvalue()
        self.assertIn('Diego Pamio', output)

    def test_cannot_print_list_for_room_not_existing(self):

        """ test unsuccessful printing of names of people in room_name that does not exist """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.print_room("Britain")
        saved = sys.stdout
        output =saved.getvalue()
        self.assertIn("Sorry.That rooms does not exist.", output)

    def test_can_print_empty_room(self):

        """ test  printing of names of people in room_name that does not exist """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.print_room("kenya")
        saved = sys.stdout
        output = saved.getvalue()
        self.assertIn("office space kenya contains no occupants", output)

    def test_successful_print_list_of_allocation_to_txt_file(self):

        """ test successful printing of names of people allocated a room to a txt file """
        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.create_room("living", ["Nairobi"])
        self.dojo.add_person('Kevin', 'Oriels', 'FELLOW')
        self.dojo.print_allocations("allocated_persons")
        self.assertTrue(os.path.isfile("allocated_persons.txt"))
        allocated_file = open("allocated_persons.txt").readlines()
        first_line = allocated_file[1]
        third_line = allocated_file[5]
        self.assertEquals(first_line, "kenya \n")
        self.assertEquals(third_line, "Kevin Oriels\n")
        # os.remove("allocated_persons.txt")

    def test_successful_print_list_of_unallocated_to_txt_file(self):

        """ test successful printing of names of people not allocated a room to a txt file """
        self.dojo = Dojo()
        self.dojo.add_person('Diego', 'Pamio', 'FELLOW')
        self.dojo.add_person('Trent', 'Renzor', 'FELLOW', 'Y')
        self.dojo.print_unallocated("unallocated_persons")
        self.assertTrue(os.path.isfile("unallocated_persons.txt"))
        unallocated_file = open("unallocated_persons.txt").readlines()
        first_line = unallocated_file[4]
        self.assertEquals(first_line, "Diego Pamio, Trent Renzor\n")
        os.remove("unallocated_persons.txt")

