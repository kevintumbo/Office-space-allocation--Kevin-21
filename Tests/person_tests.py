import unittest
from dojo import Dojo


class TestPersonCreation(unittest.TestCase):

    """ Test cases to for successful creation and failed of person(s) """

    def test_can_add_person(self):
        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.dojo.add_person('Kevin', 'Fellow', '')
        self.dojo.add_person('John', 'Staff', '')
        self.dojo.add_person('Anne', 'Fellow', 'Y')
        self.dojo.add_person('Steve', 'Fellow', 'N')
        self.assertEqual(len(self.dojo.total_people), 4, 'Person(s) were not added to the system!')

    def test_can_add_staff(self):
        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.assertEqual(len(self.dojo.staff), 0)
        self.dojo.add_person('Fred', 'Staff', '')
        self.assertEqual(len(self.dojo.staff), 1, ' staff member(s) has been added to the system!')

    def test_can_add_fellow(self):
        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.assertEqual(len(self.dojo.fellows), 0)
        self.dojo.add_person('Joe', 'Fellow', 'Y')
        self.dojo.add_person('James', 'Fellow', '')
        self.dojo.add_person('Larry', 'Fellow', 'N')
        self.assertEqual(len(self.dojo.fellows), 3, 'staff member(s) were not added to the system!')

    def test_cannot_add_person_with_missing_arguments(self):
        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.num_of_people = len(self.dojo.total_people)
        self.dojo.add_person('Kevin', '', '')
        self.dojo.add_person('', '', 'Y')
        self.dojo.add_person('', '', '')
        self.assertEqual(len(self.dojo.total_people), self.num_of_people,
                         'Person(s) created without necessary credentials')



