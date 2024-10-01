import wx
import wx.adv
from ...core.task_manager import Priority


class AddTaskDialog(wx.Dialog):
    """Dialog for adding a new task."""
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        self.SetSize(400, 300)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Task name input
        self.task_name = wx.TextCtrl(self, value="")
        sizer.Add(wx.StaticText(self, label="Task Name:"), 0, wx.ALL, 5)
        sizer.Add(self.task_name, 0, wx.ALL | wx.EXPAND, 5)

        # Task description input
        self.task_description = wx.TextCtrl(self, value="", style=wx.TE_MULTILINE)
        self.task_description.SetMinSize((-1, 100))  # Set a minimum height of 100 pixels
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
        sizer.Add(wx.StaticText(self, label="Due Date:"), 0, wx.ALL, 5)
        sizer.Add(self.due_date, 0, wx.ALL | wx.EXPAND, 5)

        # Dialog buttons
        btn_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        sizer.Add(btn_sizer, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)