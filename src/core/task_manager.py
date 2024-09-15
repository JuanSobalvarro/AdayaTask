import datetime
from peewee import Model, CharField, IntegerField, DateTimeField, SqliteDatabase
from enum import Enum
from .. import settings


# Enum for Task Priority
class Priority(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    URGENT = 3
    CRITICAL = 4


# Initialize the SQLite database connection
db = SqliteDatabase(settings.DB_PATH)


# Define the Task model using Peewee
class Task(Model):
    name = CharField()
    description = CharField(null=True)
    priority = IntegerField()
    due_datetime = DateTimeField()

    class Meta:
        database = db  # Link to the tasks.db database


class TaskManager:
    def __init__(self, db_path):
        """
        Initialize TaskManager and create the tasks table.
        """
        self.db = SqliteDatabase(db_path)
        self.connect_db()
        db.create_tables([Task])

    def connect_db(self):
        if not self.db.is_closed():
            print("Database connection is already open.")
        else:
            self.db.connect()

    def close_db(self):
        if not self.db.is_closed():
            self.db.close()

    def add_task(self, name: str, description: str, priority: Priority, due_datetime: datetime.datetime):
        """
        Add a new task to the database.
        :param name: Task name
        :param description: Task description
        :param priority: Task priority as Priority enum
        :param due_datetime: Due date and time
        """
        Task.create(
            name=name,
            description=description,
            priority=priority.value,
            due_datetime=due_datetime
        )

    def get_tasks(self):
        """
        Retrieve all tasks from the database.
        :return: List of Task objects
        """
        return list(Task.select())

    def update_task(self, task_id: int, name: str = None, description: str = None,
                    priority: Priority = None, due_datetime: datetime.datetime = None):
        """
        Update an existing task in the database.
        :param task_id: ID of the task to update
        :param name: New task name (optional)
        :param description: New task description (optional)
        :param priority: New task priority (optional)
        :param due_datetime: New task due datetime (optional)
        """
        task = Task.get(Task.id == task_id)
        if name:
            task.name = name
        if description:
            task.description = description
        if priority:
            task.priority = priority.value
        if due_datetime:
            task.due_datetime = due_datetime
        task.save()

    def delete_task(self, task_id: int):
        """
        Delete a task from the database.
        :param task_id: ID of the task to delete
        """
        task = Task.get(Task.id == task_id)
        task.delete_instance()

    def __del__(self):
        """Ensure the database connection is closed when the instance is destroyed."""
        self.close_db()