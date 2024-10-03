import wx
import datetime

from ..core.theme_manager import ThemeManager
from ..core.task_manager import TaskManager, Task, Priority  # Ensure this is imported correctly
from .customWidgets.circularCheck import CircularCheckBox
from .customWidgets.roundPanel import RoundPanel
from .dialogs.addTaskdialog import AddTaskDialog
from .dialogs.editTaskDialog import EditTaskDialog
from .dialogs.detailTaskDialog import DetailTaskDialog

class TodoPanel(wx.Panel):
    def __init__(self, parent, themeManager: ThemeManager, taskManager: TaskManager, *args, **kwds):
        super().__init__(parent, *args, **kwds)

        self.themeManager: ThemeManager = themeManager
        self.taskManager: TaskManager = taskManager  # Now receive TaskManager from MainWindow

        self.SetBackgroundColour(self.themeManager.get_color('bg'))

        # List to track the checkboxes and their associated tasks
        self.task_checkboxes = []

        # Main vertical sizer for the panel
        self.task_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.task_sizer)

        # Load tasks and buttons
        self.__loadAll()

    def __loadAll(self):
        self.__load_tasks()
        self.__add_task_buttons()

    def __add_task_buttons(self):
        # Add a stretchable spacer before the buttons to keep them at the bottom
        self.task_sizer.AddStretchSpacer(1)

        # Sizer to hold the buttons at the bottom of the panel
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Add Task Button
        self.add_task_button = wx.Button(self, label="Add Task")
        self.add_task_button.SetBackgroundColour(self.themeManager.get_color('button1'))
        self.add_task_button.SetForegroundColour(self.themeManager.get_color('text1'))
        self.add_task_button.SetFont(self.themeManager.get_font('button'))
        self.add_task_button.Bind(wx.EVT_BUTTON, self.__on_add_task)
        button_sizer.Add(self.add_task_button, 0, wx.ALL | wx.CENTER, 10)

        # Clean Selected Button
        self.clean_selected_button = wx.Button(self, label="Clean Selected")
        self.clean_selected_button.SetBackgroundColour(self.themeManager.get_color('button1'))
        self.clean_selected_button.SetForegroundColour(self.themeManager.get_color('text1'))
        self.clean_selected_button.SetFont(self.themeManager.get_font('button'))
        self.clean_selected_button.Bind(wx.EVT_BUTTON, self.__on_clean_selected)
        button_sizer.Add(self.clean_selected_button, 0, wx.ALL | wx.CENTER, 10)

        # Add the button sizer to the main panel
        self.task_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)

        self.Layout()

    def __load_tasks(self):
        """
        Load tasks from the TaskManager and display them.
        """
        self.task_sizer.Clear(True)  # Clear the sizer and remove all current task panels
        self.task_checkboxes.clear()  # Clear the checkboxes list

        # Fetch all tasks from the task manager and display them
        for task in self.taskManager.tasks:
            self.__display_task(task)

        self.Layout()

    def __display_task(self, task: Task):
        """
        Display a task in the task list with priority-indicated colors.
        """
        task_panel = wx.Panel(self)
        # task_panel.SetBackgroundColour(Priority.get_priority_color(task.priority))
        task_panel.SetBackgroundColour(self.themeManager.get_color('bg'))
        task_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Custom Circular Checkbox
        check = CircularCheckBox(task_panel, radius=12, check_proportion=0.6,
                                 bg_color=self.themeManager.get_color('bg'),
                                 inner_bg_color=self.themeManager.get_color('bg'),
                                 check_color=self.themeManager.get_color('check1'))
        task_sizer.Add(check, 0, wx.ALL | wx.CENTER, 5)

        # Track the checkbox with the associated task
        self.task_checkboxes.append((check, task))

        # Task Label with Priority Color
        task_color = Priority.get_priority_color(task.priority)
        task_label_panel = RoundPanel(task_panel, radius=10,
                                bg_color=self.themeManager.get_color('bg'),
                                inner_bg_color=task_color,
                                border=0)
        # task_label_panel.SetBackgroundColour(task_color)

        task_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        task_label = wx.StaticText(task_label_panel, label=task.name)
        task_label.SetBackgroundColour(task_color)
        task_label.SetFont(self.themeManager.get_font('body'))
        task_label_sizer.Add(task_label, 1, wx.ALL | wx.CENTER, 10)

        task_label_panel.SetSizer(task_label_sizer)
        task_sizer.Add(task_label_panel, 1, wx.ALL | wx.EXPAND, 5)

        # Edit Button with Rounded Corners
        edit_button = wx.Button(task_panel, label="Edit")
        edit_button.SetBackgroundColour(self.themeManager.get_color('button1'))
        edit_button.SetForegroundColour(self.themeManager.get_color('text1'))
        edit_button.SetFont(self.themeManager.get_font('button'))

        task_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5)

        task_panel.SetSizer(task_sizer)
        self.task_sizer.Add(task_panel, 0, wx.EXPAND | wx.ALL, 5)

        # Bind events
        self.__bind_click_recursive(task_label_panel, task)
        edit_button.Bind(wx.EVT_BUTTON, lambda evt, t=task: self.__on_edit_task(evt, t))

        self.Layout()

    def __bind_click_recursive(self, widget, task):
        """
        Recursively binds a click event to the widget and all its children.
        This ensures the task panel responds to clicks even on its child widgets.
        """
        widget.Bind(wx.EVT_LEFT_UP, lambda event: self.__on_task_details(task))

        for child in widget.GetChildren():
            self.__bind_click_recursive(child, task)

    def __on_clean_selected(self, event):
        """Handler for cleaning all selected tasks."""
        # Create a list of tasks to remove
        tasks_to_remove = [task for check, task in self.task_checkboxes if check.is_checked()]

        # Remove the selected tasks from the task manager
        for task in tasks_to_remove:
            self.taskManager.remove_task(task)

        # Reload the tasks
        self.__load_tasks()
        self.__add_task_buttons()

    def __on_task_details(self, task):
        """
        Show the TaskDetailDialog when the task panel is clicked.
        """
        dialog = DetailTaskDialog(task, self.themeManager, parent=self)
        dialog.ShowModal()
        dialog.Destroy()

    def __on_add_task(self, event):
        """
        Handler for adding a new task.
        """
        dialog = AddTaskDialog(parent=self, theme_manager=self.themeManager)
        new_task = dialog.create_task()

        if new_task is not None:
            self.taskManager.add_task(new_task)

        self.__loadAll()

    def __on_edit_task(self, event, task):
        """
        Handler for edit an existing task.
        """
        dialog = EditTaskDialog(parent=self, theme_manager=self.themeManager, task=task)
        updated_task = dialog.update_task()

        if updated_task is not None:
            self.taskManager.update_tasks()

        self.__loadAll()
