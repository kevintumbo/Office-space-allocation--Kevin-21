import unittest
from dojo import Dojo


class TestRoomCreation(unittest.TestCase):

    """ Test cases to for successful and failed room creation """

    def test_can_create_office(self):

        """ Test successful creation of office space"""

        self.dojo = Dojo()
        self.assertEqual(len(self.dojo.total_rooms), 0)
        self.dojo.create_room('office', ['marylin'])
        self.assertEqual(len(self.dojo.total_rooms), 1, 'An office has been successfully created!')

    def test_can_create_living_space(self):

        """ Test successful creation of living space"""

        self.dojo = Dojo()
        self.assertEqual(len(self.dojo.total_rooms), 0)
        self.dojo.create_room('living', ['manson'])
        self.assertEqual(len(self.dojo.total_rooms), 1, 'A living space has been successfully created!')

    def test_can_create_multiple_office(self):

        """ Test successful creation of multiple offices """

        self.dojo = Dojo()
        self.assertEqual(len(self.dojo.total_rooms), 0)
        self.dojo.create_room('office', ['Texas', 'Alabama', 'Chicago', 'Memphis'])
        self.assertEqual(len(self.dojo.total_rooms), 4, 'offices have been successfully created!')

    def test_can_create_multiple_living_space(self):

        """ Test successful creation of multiple living spaces """

        self.dojo = Dojo()
        self.assertEqual(len(self.dojo.total_rooms), 0)
        self.dojo.create_room('living', ['Kenya', 'Uganda', 'Tanzania', 'Rwanda'])
        self.assertEqual(len(self.dojo.total_rooms), 4, 'living spaces have been successfully created!')

    def test_cannot_duplicate_room(self):

        """ Test failure in creation of rooms with duplicate names """

        self.dojo = Dojo()
        self.assertEqual(len(self.dojo.total_rooms), 0)
        self.total_num_of_rooms = len(self.dojo.total_rooms)
        self.dojo.create_room('living', ['Kenya'])
        self.dojo.create_room('office', ['Kenya'])
        self.dojo.create_room('living', ['Kenya'])
        self.assertEqual(len(self.dojo.total_rooms), 1,
                         'Rooms cannot have duplicate names!')

    def test_cannot_create_room_when_arguments_are_missing(self):

        """ Test failure in creation of rooms with Missing arguments """

        self.dojo = Dojo()
        self.total_num_of_rooms = len(self.dojo.total_rooms)
        self.dojo.create_room('office', [])
        self.dojo.create_room('living', [])
        self.dojo.create_room('', '')
        self.dojo.create_room('2345', '2243')
        self.dojo.create_room('', 'marylin')
        self.dojo.create_room('Bathroom', ['', '', ''])
        self.assertEqual(len(self.dojo.total_rooms), self.total_num_of_rooms,
                         ' rooms cannot be created without necessary credentials')



