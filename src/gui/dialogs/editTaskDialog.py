import wx
import wx.adv
import datetime
from ...core.task_manager import Priority, Task
from ...core.theme_manager import ThemeManager


class EditTaskDialog(wx.Dialog):
    """
    Dialog for editing an existing task.
    """
    def __init__(self, theme_manager: ThemeManager, task: Task, *args, **kwds):
        super().__init__(*args, **kwds)

        self.themeManager = theme_manager
        self.task = task

        self.SetTitle("Edit Task")
        self.SetSize(400, 400)
        self.SetBackgroundColour(self.themeManager.get_color('bg'))

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Task name input (pre-filled with the task's current name)
        self.task_name = wx.TextCtrl(self, value=self.task.name)
        sizer.Add(wx.StaticText(self, label="Task Name:"), 0, wx.ALL, 5)
        sizer.Add(self.task_name, 0, wx.ALL | wx.EXPAND, 5)

        # Task description input (pre-filled with the task's current description)
        self.task_description = wx.TextCtrl(self, value=self.task.description, style=wx.TE_MULTILINE)
        self.task_description.SetMinSize((0, 100))  # Set a minimum height of 100 pixels
        sizer.Add(wx.StaticText(self, label="Description:"), 0, wx.ALL, 5)
        sizer.Add(self.task_description, 1, wx.ALL | wx.EXPAND, 5)

        # Priority selection (pre-selected with the task's current priority)
        priorities = [p.name for p in Priority]
        self.priority_choice = wx.Choice(self, choices=priorities)
        self.priority_choice.SetSelection(self.task.priority.value)  # Assuming Priority is an enum with value mapping
        sizer.Add(wx.StaticText(self, label="Priority:"), 0, wx.ALL, 5)
        sizer.Add(self.priority_choice, 0, wx.ALL | wx.EXPAND, 5)

        # Due date and time (pre-filled with the task's current due date and time)
        self.due_date = wx.adv.DatePickerCtrl(self)
        self.due_time = wx.adv.TimePickerCtrl(self)
        due_date = self.task.due_datetime.date()
        due_time = self.task.due_datetime.time()
        self.due_date.SetValue(wx.DateTime.FromDMY(due_date.day, due_date.month - 1, due_date.year))
        self.due_time.SetTime(due_time.hour, due_time.minute, due_time.second)

        sizer.Add(wx.StaticText(self, label="Due Date:"), 0, wx.ALL, 5)
        sizer.Add(self.due_date, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(wx.StaticText(self, label="Due Time:"), 0, wx.ALL, 5)
        sizer.Add(self.due_time, 0, wx.ALL | wx.EXPAND, 5)

        # Dialog buttons
        btn_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        sizer.Add(btn_sizer, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)
        self.Layout()

    def update_task(self):
        """
        Updates the task based on the dialog inputs. Returns the updated task if OK is pressed, None otherwise.
        """
        updated_task = None
        if self.ShowModal() == wx.ID_OK:
            self.task.name = self.task_name.GetValue()
            self.task.description = self.task_description.GetValue()
            self.task.priority = Priority(self.priority_choice.GetSelection())  # Assuming enum mapping

            wx_datetime = self.due_date.GetValue()
            wx_time = self.due_time.GetValue()
            
            py_datetime = datetime.datetime(wx_datetime.year, wx_datetime.month + 1, wx_datetime.day,
                                            wx_time.GetHour(), wx_time.GetMinute(), wx_time.GetSecond())

            self.task.due_datetime = py_datetime
            updated_task = self.task

        self.Destroy()
        return updated_task
