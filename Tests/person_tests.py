import unittest
from dojo import Dojo


class TestPersonCreation(unittest.TestCase):

    """ Test cases to for successful creation and failed of person(s) """

    def test_can_add_person(self):

        """ Test successful addition of person """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.dojo.add_person('Kevin', 'Oriels', 'FELLOW')
        self.dojo.add_person('John', 'john', 'STAFF', '')
        self.dojo.add_person('Anne', 'Ndinda', 'FELLOW', 'Y')
        self.dojo.add_person('Steve', 'Mcmon', 'FELLOW', 'N')
        self.assertEqual(len(self.dojo.total_people), 4, 'Person(s) were added to the system!')

    def test_can_add_staff(self):

        """ Test successful addition of staff """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.assertEqual(len(self.dojo.total_people), 0)
        self.dojo.add_person('Fred', 'Flint', 'STAFF')
        self.assertEqual(len(self.dojo.total_people), 1, ' staff member(s) has been added to the system!')

    def test_can_add_fellow(self):

        """ Test successful addition of fellows"""

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya", "uganda"])
        self.dojo.create_room("living", ["Nairobi", "Kampala"])
        self.assertEqual(len(self.dojo.total_people), 0)
        self.dojo.add_person('Joe', 'jameson', 'FELLOW', 'Y')
        self.dojo.add_person('James', 'konia', 'FELLOW')
        self.dojo.add_person('Larry', 'smith', 'FELLOW', 'N')
        self.assertEqual(len(self.dojo.total_people), 3, 'staff member(s) were added to the system!')

    def test_cannot_add_duplicate_name(self):
        self.dojo = Dojo()
        self.dojo.add_person('James', 'konia', 'FELLOW')
        self.dojo.add_person('James', 'konia', 'FELLOW')
        self.assertEqual(len(self.dojo.total_people), 1)

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

    def test_successful_loading_of_people_using_a_txt_file(self):
        """ Test for successful addition of person(s) from a txt file """

        self.dojo = Dojo()
        self.dojo.load_people("sample")
        self.assertEqual(len(self.dojo.total_people), 7)

    def test_unsuccessful_loading_of_people_due_to_missing_text_file(self):
        """ Test for unsuccessful addition of person(s) due to missing text file """

        self.dojo = Dojo()
        load = self.dojo.load_people("sample2")
        self.assertEqual(len(self.dojo.total_people), 0)
        self.assertEquals(load, "Sorry that file does not exist")

    def test_unsuccessful_loading_of_people_due_to_wrong_format_in_text_file(self):
        """ Test for unsuccessful addition of person(s) due to wrong format in text file """

        self.dojo = Dojo()
        self.dojo.load_people("wrong_format")
        self.assertEqual(len(self.dojo.total_people), 0)


class TestReallocatePerson(unittest.TestCase):
    """ Test cases to for successful reallocation and failed reallocation of person(s) """

    def test_can_successfully_reallocate_person_from_one_office_to_another(self):
        """ Test successful reallocation of person from one office to another"""

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('James', 'konia', 'FELLOW')
        self.dojo.create_room("office", ["Uganda"])
        self.dojo.reallocate_person("James", "konia", "Uganda")
        self.assertTrue(len(self.dojo.total_rooms[0].occupants) == 0)
        self.assertTrue(len(self.dojo.total_rooms[1].occupants) == 1)

    def test_can_successfully_reallocate_fellow_from_one_living_space_to_another(self):
        """ Test successful reallocation of person from one living space to another """

        self.dojo = Dojo()
        self.dojo.create_room("living", ["Kampala"])
        self.dojo.create_room("office", ["Kenya"])
        self.dojo.add_person('Akira', 'Menai', 'FELLOW', 'Y')
        self.dojo.add_person('rex', 'acey', 'FELLOW', 'Y')
        self.dojo.create_room("living", ["Nairobi"])
        self.dojo.reallocate_person("Akira", "Menai", "Nairobi")
        self.assertTrue(len(self.dojo.total_rooms[0].occupants) == 1)
        self.assertTrue(len(self.dojo.total_rooms[2].occupants) == 1)

    def test_can_successfully_reallocate_person_on_waiting_list_a_room(self):
        """ Test successful reallocation of person on waiting list a room  """

        self.dojo = Dojo()
        self.dojo.add_person('James', 'macavoy', 'FELLOW', 'Y')
        self.dojo.create_room("office", ["kenya"])
        self.dojo.create_room("living", ["Kampala"])
        self.dojo.reallocate_person("James", "macavoy", "kenya")
        self.dojo.reallocate_person("James", "macavoy", "Kampala")
        self.assertTrue(len(self.dojo.total_rooms[0].occupants) == 1)
        self.assertTrue(len(self.dojo.total_rooms[1].occupants) == 1)

    def test_cannot_reallocate_person_if_person_does_not_exist(self):
        """ Test failure when reallocating person who does not exist """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Ian', 'pyr', 'FELLOW', 'Y')
        msg1 = self.dojo.reallocate_person("James", "macavoy", "kenya")
        self.assertEquals(msg1, "Sorry that person does not exist")

    def test_cannot_reallocate_person_if_room_does_not_exist(self):
        """ Test failure when reallocating person to room that does not exist """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('chris', 'Jaba', 'FELLOW', 'Y')
        self.dojo.create_room("office", ["Somalia"])
        msg1 = self.dojo.reallocate_person("chris", "Jaba", "Ghana")
        self.assertEquals(msg1, "Sorry that room does not exist")

    def test_cannot_reallocate_person_in_room_with_maximum_occupants(self):
        """ Test failure when reallocating person to room at maximum capacity """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Ian', 'pyr', 'FELLOW')
        self.dojo.add_person('Joe', 'jameson', 'FELLOW')
        self.dojo.add_person('Ruben', 'konia', 'FELLOW')
        self.dojo.add_person('James', 'macavoy', 'FELLOW')
        self.dojo.add_person('Akira', 'Menai', 'FELLOW')
        self.dojo.add_person('rex', 'acey', 'FELLOW')
        self.assertTrue(len(self.dojo.total_rooms[0].occupants) == 6)
        self.dojo.add_person('Larry', 'smith', 'FELLOW')
        msg1 = self.dojo.reallocate_person("Larry", "smith", "kenya")
        self.assertEquals(msg1, "sorry that room is full")

    def test_cannot_rellocate_staff_living_space(self):
        """ Test failure when reallocating staff to reallocate staff to living space """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.create_room("living", ["Kampala"])
        self.dojo.add_person('Armin', 'Buren', 'STAFF')
        msg = self.dojo.reallocate_person("Armin", "Buren", "Kampala")
        self.assertEquals(msg, "Sorry.staff cannot be allowed in living space")

    def test_cannot_reallocate_to_same_room(self):
        """ Test failure when trying to reallocate person to same room """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.add_person('Armin', 'Buren', 'STAFF')
        msg1 = self.dojo.reallocate_person("Armin", "Buren", "kenya")
        self.assertEquals(msg1, "sorry. you cannot reallocate to the same room")
        self.dojo.create_room("living", ["Nairobi"])
        self.dojo.add_person('Joel', 'Ortiz', 'FELLOW', 'Y')
        msg2 = self.dojo.reallocate_person("Joel", "Ortiz", "Nairobi")
        self.assertEquals(msg2, "sorry. you cannot reallocate to the same room")
