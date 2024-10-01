import datetime
from enum import Enum
import yaml
import os
from .. import settings


# Enum for Task Priority
class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    URGENT = 3
    CRITICAL = 4

    @staticmethod
    def get_priority_color(priority):
        """
        Get the background color based on task priority.
        """
        priority_colors = {
            Priority.LOW: '#E0E5EC',
            Priority.MEDIUM: '#FFD580',
            Priority.HIGH: '#FFB347',
            Priority.URGENT: '#FF6961',
            Priority.CRITICAL: '#FF3F3F'
        }
        return priority_colors.get(priority, '#FFFFFF')


class Task:
    def __init__(self, name: str, priority: Priority, description: str, due_datetime: datetime.datetime):
        self.name = name
        self.priority = priority
        self.description = description
        self.due_datetime = due_datetime

    def to_dict(self):
        """
        Convert Task object to a dictionary for YAML serialization
        """
        return {
            'name': self.name,
            'priority': self.priority.name,  # Save the name of the priority (e.g., 'HIGH')
            'description': self.description,
            'due_datetime': self.due_datetime.isoformat()
        }

    @staticmethod
    def from_dict(data):
        """
        Create Task object from dictionary data
        """
        return Task(
            name=data['name'],
            priority=Priority[data['priority']],  # Convert priority name back to enum
            description=data['description'],
            due_datetime=datetime.datetime.fromisoformat(data['due_datetime'])  # Convert string back to datetime
        )


class TaskManager:
    def __init__(self, path_tasks=os.path.join(settings.BASE_DIR, 'tasks', 'tasks.yaml')):
        """
        Initialize TaskManager and load tasks from YAML file.
        """
        self.path_tasks = path_tasks
        self.tasks = []

        # Load tasks from YAML file on initialization
        self.__load_tasks()

    def get_tasks(self) -> list[Task]:
        """
        Returns a list of tasks
        """
        return self.tasks

    def add_task(self, task: Task):
        """
        Add a task to the task list and save the updated list to YAML file
        """
        self.tasks.append(task)
        self.__save_tasks()

    def update_tasks(self):
        """
        Update the tasks by saving the current task list to the YAML file.
        """
        self.__save_tasks()

    def remove_task(self, task: Task):
        """
        Remove a task from the task list and save the updated list to YAML file
        """
        if task in self.tasks:
            self.tasks.remove(task)
        self.__save_tasks()

    def __load_tasks(self):
        """
        Load the tasks from the YAML file into the tasks list.
        """
        if os.path.exists(self.path_tasks):
            with open(self.path_tasks, 'r') as file:
                tasks_data = yaml.load(file, Loader=yaml.SafeLoader)
                if tasks_data:
                    self.tasks = [Task.from_dict(task) for task in tasks_data]

    def __save_tasks(self):
        """
        Save the current list of tasks to the YAML file.
        """
        with open(self.path_tasks, 'w') as file:
            yaml.dump([task.to_dict() for task in self.tasks], file)

    def clear_tasks(self):
        """
        Clear the tasks list and delete the tasks from the YAML file.
        """
        self.tasks = []
        with open(self.path_tasks, 'w') as file:
            file.truncate(0)  # Clear the file content
