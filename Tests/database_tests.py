import unittest
import os
import sqlite3
from dojo import Dojo


class TestSaveState(unittest.TestCase):

    """ Test cases for state to database(s) """

    def test_successful_save_state_creates_database_without_db_name(self):

        """ Test successful creation of default database file dojo.db """

        self.dojo = Dojo()
        self.assertTrue(os.path.isfile("dojo.db"))
        os.remove("dojo.db")

    def test_successful_save_state_creates_database_with_db_name(self):

        """ Test successful creation of database file with db_name as its name """

        self.dojo = Dojo()
        self.dojo.save_state("january_data")
        self.assertTrue(os.path.isfile("january_data.db"))
        os.remove("january_data.db")

    def test_save_state_succesfully_stores_data_in_database(self):

        """ Test successful storage of data from app into database using the save_state method """

        self.dojo = Dojo()
        self.dojo.create_room("office", ["kenya"])
        self.dojo.create_room("living", ["Kampala"])
        self.dojo.load_people("sample")
        msg = self.dojo.save_state('test')
        self.assertTrue(os.path.isfile("test.db"))
        self.assertEqual(msg, "You have saved data to the database")
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        name = ('OLUWAFEMI SULE',)
        c.execute('SELECT * FROM people WHERE name=?', name)
        row = c.fetchone()
        assert row[1] == 'OLUWAFEMI SULE'
        assert row[2] == 'FELLOW'
        assert row[3] == 'Y'
        assert row[4] == 'kenya'
        assert row[5] == 'Kampala'
        conn.close()
        os.remove("test.db")


class TestLoadState(unittest.TestCase):

    """ Test cases for successful and failed save state to database(s) """

    def test_successful_load_of_database_into_app(self):

        """ Test successful loading of data from database into from app using the load_state method """

        self.dojo = Dojo()
        self.assertTrue(os.path.isfile("dojo_test.db"))
        msg = self.dojo.load_state("dojo_test")
        self.assertEqual(msg, "database has been loaded")
        self.assertTrue(len(self.dojo.total_rooms) == 2)
        self.assertTrue(len(self.dojo.total_people) == 7)
        self.assertTrue(len(self.dojo.waiting_for_office_allocation) == 1)
        self.assertTrue(len(self.dojo.waiting_for_living_space_allocation) == 1)

    def test_failure_when_loading_database_that_does_not_exist(self):

        """ test failure when trying to load database file that does not exist """

        self.dojo = Dojo()
        msg = self.dojo.load_state("fake")
        self.assertEqual(msg, "Sorry that database file cannot be found")
