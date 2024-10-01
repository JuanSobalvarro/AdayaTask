import unittest
import datetime
import os
from ..task_manager import Task, TaskManager, Priority
from ... import settings


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """
        Set up the task manager with a temporary YAML file for testing.
        """
        # Create a test YAML file in the 'tasks' directory
        self.test_path = os.path.join(settings.BASE_DIR, 'tasks', 'test_tasks.yaml')
        self.manager = TaskManager(path_tasks=self.test_path)

        # Ensure the test file starts off empty
        self.manager.clear_tasks()

    def tearDown(self):
        """
        Clean up by deleting the test YAML file.
        """
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    def test_add_task(self):
        """
        Test adding a task and check if it is saved correctly.
        """
        # Create a sample task
        task = Task(name="Test Task", priority=Priority.MEDIUM, description="This is a test task.",
                    due_datetime=datetime.datetime(2024, 10, 1, 12, 0))

        # Add task to manager
        self.manager.add_task(task)

        # Ensure task is added
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].name, "Test Task")

    def test_save_and_load_tasks(self):
        """
        Test saving and loading tasks from the YAML file.
        """
        # Create a sample task and add it to the manager
        task = Task(name="Test Save Task", priority=Priority.HIGH, description="This is a test save task.",
                    due_datetime=datetime.datetime(2024, 10, 2, 15, 30))
        self.manager.add_task(task)

        # Create a new manager instance that loads from the same file
        new_manager = TaskManager(path_tasks=self.test_path)

        # Ensure the task was loaded correctly from the file
        self.assertEqual(len(new_manager.tasks), 1)
        self.assertEqual(new_manager.tasks[0].name, "Test Save Task")
        self.assertEqual(new_manager.tasks[0].priority, Priority.HIGH)

    def test_clear_tasks(self):
        """
        Test clearing tasks both in memory and in the YAML file.
        """
        # Add some tasks
        task1 = Task(name="Task 1", priority=Priority.LOW, description="Test task 1.",
                     due_datetime=datetime.datetime(2024, 9, 30))
        task2 = Task(name="Task 2", priority=Priority.URGENT, description="Test task 2.",
                     due_datetime=datetime.datetime(2024, 9, 30))

        self.manager.add_task(task1)
        self.manager.add_task(task2)

        # Clear all tasks
        self.manager.clear_tasks()

        # Check that tasks list is empty
        self.assertEqual(len(self.manager.tasks), 0)

        # Create a new manager instance and ensure tasks file is cleared
        new_manager = TaskManager(path_tasks=self.test_path)
        self.assertEqual(len(new_manager.tasks), 0)


if __name__ == "__main__":
    unittest.main()
