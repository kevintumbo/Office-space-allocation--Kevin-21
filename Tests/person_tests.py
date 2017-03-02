import unittest
from dojo import Dojo


class TestPersonCreation(unittest.TestCase):

    """ Test cases to for successful creation and failed of person(s) """

    def setup(self):
        self.dojo = Dojo()

    def test_can_add_person(self):
        self.assertEqual(len(self.dojo.total_people), 0)
        self.dojo.add_person('Kevin', 'Fellow')
        self.dojo.add_person('John', 'Staff')
        self.dojo.add_person('Anne', 'Fellow', 'Y')
        self.dojo.add_person('Steve', 'Fellow', 'N')
        self.assertEqual(len(self.dojo.total_people), 4, 'people were successfully added to the system!')

    def test_can_add_staff(self):
        self.assertEqual(len(self.dojo.staff), 0)
        self.dojo.add_person('Fred', 'Staff')
        self.assertEqual(len(self.dojo.staff), 1, 'A new staff member has been added to the system!')

    def test_can_add_fellow(self):
        self.assertEqual(len(self.dojo.fellows), 0)
        self.dojo.add_person('Joe', 'Fellow', 'Y')
        self.dojo.add_person('James', 'Fellow')
        self.dojo.add_person('Larry', 'Fellow', 'N')
        self.assertEqual(len(self.dojo.fellows), 3, 'staff members has been added to the system!')

    def test_cannot_add_person_with_missing_arguments(self):
        self.num_of_people = len(self.dojo.total_people)
        self.dojo.add_person('Kevin', '')
        self.dojo.add_person('', 'Staff')
        self.dojo.add_person('', '', 'Y')
        self.dojo.add_person('', '', '')
        self.dojo.add_person('', 'Fellow', 'N')
        self.assertEqual(len(self.dojo.total_people), self.num_of_people,
                         'Person(s) created without necessary credentials')

    def test_staff_cannot_be_allocated_space(self):
        self.num_of_stuff = len(self.dojo.staff)
        self.dojo.add_person('Judas', 'Staff', 'Y')
        self.assertEqual(len(self.dojo.staff), self.num_of_stuff,
                         'Staff allocated living space')

    def tearDown(self):
        self.dojo.__del__()

