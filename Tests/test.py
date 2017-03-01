import unittest
from dojo import Dojo


class TestRoomCreation(unittest.TestCase):

    """ Test cases to for successful room creation """

    def setup(self):
        self.dojo = Dojo()

    def test_can_create_office(self):
        self.assertEqual(len(self.dojo.offices), 0)
        self.dojo.create_room('office', 'marylin')
        self.assertEqual(len(self.dojo.offices), 1, 'An office has been successfully created!')

    def test_can_create_livingspace(self):
        self.assertEqual(len(self.dojo.livingspaces), 0)
        self.dojo.create_room('livingspace', 'manson')
        self.assertEqual(len(self.dojo.livingspaces), 1, 'A living space has been successfully created!')

    def test_can_create_multiple_office(self):
        self.assertEqual(len(self.dojo.offices), 0)
        self.dojo.create_room('office', ['Texas', 'Alabama', 'Chicago', 'Memphis'])
        self.assertEqual(len(self.dojo.offices), 4, 'offices has been successfully created!')

    def test_can_create_multiple_livingspace(self):
        self.assertEqual(len(self.dojo.livingspaces), 0)
        self.dojo.create_room('livingspace', ['Kenya', 'Uganda', 'Tanzania', 'Rwanda'])
        self.assertEqual(len(self.dojo.livingspaces), 1, 'living spaces has been successfully created!')


class TestPersonCreation(unittest.TestCase):

    """ Test cases to for successful room creation """

    def setup(self):
        self.dojo = Dojo()

    def test_can_add_person(self):
        self.assertEqual(len(self.dojo.total_people), 0)
        self.dojo.add_person('Kevin', 'Fellow')
        self.dojo.add_person('John', 'Staff')
        self.dojo.add_person('Anne', 'Fellow', 'yes')
        self.dojo.add_person('Steve', 'Fellow', 'No')
        self.assertEqual(len(self.dojo.total_people), 4, 'people were successfully added to the system!')

    def test_can_add_staff(self):
        self.assertEqual(len(self.dojo.staff), 0)
        self.dojo.add_person('Fred', 'Staff')
        self.assertEqual(len(self.dojo.staff), 1, 'A new staff member has been added to the system!')

    def test_can_add_fellow(self):
        self.assertEqual(len(self.dojo.fellows), 0)
        self.dojo.add_person('Joe', 'Fellow', 'yes')
        self.dojo.add_person('James', 'Fellow')
        self.dojo.add_person('Larry', 'Fellow', 'No')
        self.assertEqual(len(self.dojo.fellows), 3, 'staff members has been added to the system!')
