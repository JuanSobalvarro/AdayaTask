import unittest
import datetime
from peewee import SqliteDatabase
from ..task_manager import Task, TaskManager, Priority


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """
        Set up an in-memory SQLite database and create the tasks table.
        """
        # Use an in-memory SQLite database for testing
        self.manager = TaskManager(db_path=':memory:')

    def tearDown(self):
        """
        Tear down the test database connection.
        """
        self.manager.close_db()




if __name__ == "__main__":
    unittest.main()
