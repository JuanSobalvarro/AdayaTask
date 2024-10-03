import wx
import wx.adv
import datetime
from ...core.task_manager import Priority, Task
from ...core.theme_manager import ThemeManager


class AddTaskDialog(wx.Dialog):
    """
    Dialog for adding a new task.
    """
    def __init__(self, theme_manager: ThemeManager, *args, **kwds):
        super().__init__(*args, **kwds)

        self.themeManager = theme_manager

        self.SetTitle("Add Task")
        self.SetSize(400, 400)
        self.SetBackgroundColour(self.themeManager.get_color('bg'))

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Task name input
        self.task_name = wx.TextCtrl(self, value="")
        sizer.Add(wx.StaticText(self, label="Task Name:"), 0, wx.ALL, 5)
        sizer.Add(self.task_name, 0, wx.ALL | wx.EXPAND, 5)

        # Task description input
        self.task_description = wx.TextCtrl(self, value="", style=wx.TE_MULTILINE)
        self.task_description.SetMinSize((0, 100))  # Set a minimum height of 100 pixels
        sizer.Add(wx.StaticText(self, label="Description:"), 0, wx.ALL, 5)
        sizer.Add(self.task_description, 1, wx.ALL | wx.EXPAND, 5)

        # Priority selection
        priorities = [p.name for p in Priority]
        self.priority_choice = wx.Choice(self, choices=priorities)
        self.priority_choice.SetSelection(0)
        sizer.Add(wx.StaticText(self, label="Priority:"), 0, wx.ALL, 5)
        sizer.Add(self.priority_choice, 0, wx.ALL | wx.EXPAND, 5)

        # Due date
        self.due_date = wx.adv.DatePickerCtrl(self)
        self.due_time = wx.adv.TimePickerCtrl(self)
        sizer.Add(wx.StaticText(self, label="Due Date:"), 0, wx.ALL, 5)
        sizer.Add(self.due_date, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(wx.StaticText(self, label="Due Time:"), 0, wx.ALL, 5)
        sizer.Add(self.due_time, 0, wx.ALL | wx.EXPAND, 5)

        # Dialog buttons
        btn_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        sizer.Add(btn_sizer, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)
        self.Layout()
        # self.Fit()

    def create_task(self):
        """
        Creates a new task base on the dialog answer, if it is ok it returns a task with the values,
        else it returns None.
        """
        new_task = None
        if self.ShowModal() == wx.ID_OK:
            name = self.task_name.GetValue()
            description = self.task_description.GetValue()
            priority = Priority(self.priority_choice.GetSelection())  # Assuming selections correspond to enum
            wx_datetime = self.due_date.GetValue()
            py_datetime = datetime.datetime(wx_datetime.year, wx_datetime.month, wx_datetime.day)

            new_task = Task(name=name, priority=priority, description=description, due_datetime=py_datetime)

        self.Destroy()
        return new_task