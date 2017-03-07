import unittest
from dojo import Dojo


class TestPersonCreation(unittest.TestCase):

    """ Test cases to for successful creation and failed of person(s) """

    def test_can_add_person(self):

        """ Test successful addition of person """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.dojo.add_person('Kevin', 'Oriels', 'Fellow')
        self.dojo.add_person('John', 'john', 'Staff', '')
        self.dojo.add_person('Anne', 'Ndinda', 'Fellow', 'Y')
        self.dojo.add_person('Steve', 'Mcmon', 'Fellow', 'N')
        self.assertEqual(len(self.dojo.total_people), 4, 'Person(s) were added to the system!')

    def test_can_add_staff(self):

        """ Test successful addition of staff """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.assertEqual(len(self.dojo.total_people), 0)
        self.dojo.add_person('Fred', 'Flint', 'Staff')
        self.assertEqual(len(self.dojo.total_people), 1, ' staff member(s) has been added to the system!')

    def test_can_add_fellow(self):

        """ Test successful addition of fellows"""

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.assertEqual(len(self.dojo.total_people), 0)
        self.dojo.add_person('Joe', 'jameson','Fellow', 'Y')
        self.dojo.add_person('James', 'konia','Fellow')
        self.dojo.add_person('Larry', 'smith','Fellow', 'N')
        self.assertEqual(len(self.dojo.total_people), 3, 'staff member(s) were added to the system!')

    def test_cannot_add_person_with_missing_arguments(self):

        """ Test failure in addition of persons with Missing arguments """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.num_of_people = len(self.dojo.total_people)
        self.dojo.add_person('Kevin', '', '')
        self.dojo.add_person('', '', '', 'Y')
        self.dojo.add_person('', '', '', '')
        self.assertEqual(len(self.dojo.total_people), self.num_of_people,
                         'Person(s) cannot be created without necessary credentials')
