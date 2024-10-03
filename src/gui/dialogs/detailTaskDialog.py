import wx
import wx.adv
from ...core.task_manager import Task
from ...core.theme_manager import ThemeManager


class DetailTaskDialog(wx.Dialog):
    """
    Dialog for displaying task details.
    """

    def __init__(self, task: Task, theme_manager: ThemeManager, *args, **kwds):
        super().__init__(*args, **kwds)

        self.themeManager = theme_manager
        self.task = task

        self.SetTitle("Task Details")
        self.SetBackgroundColour(self.themeManager.get_color('bg'))
        self.SetSize(400, 500)  # Adjust the size according to your design needs

        # Main sizer for the dialog
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Task Name
        name_label = wx.StaticText(self, label="Task Name:", style=wx.ALIGN_LEFT)
        name_label.SetFont(self.themeManager.get_font('heading'))
        main_sizer.Add(name_label, 0, wx.ALL | wx.EXPAND, 10)

        task_name = wx.StaticText(self, label=self.task.name)
        task_name.SetFont(self.themeManager.get_font('body'))
        main_sizer.Add(task_name, 0, wx.ALL | wx.EXPAND, 10)

        # Task Description
        desc_label = wx.StaticText(self, label="Description:", style=wx.ALIGN_LEFT)
        desc_label.SetFont(self.themeManager.get_font('heading'))
        main_sizer.Add(desc_label, 0, wx.ALL | wx.EXPAND, 10)

        task_description = wx.TextCtrl(self, value=self.task.description, style=wx.TE_MULTILINE | wx.TE_READONLY)
        task_description.SetBackgroundColour(self.themeManager.get_color('bg'))
        main_sizer.Add(task_description, 1, wx.ALL | wx.EXPAND, 10)

        # Task Priority
        priority_label = wx.StaticText(self, label="Priority:", style=wx.ALIGN_LEFT)
        priority_label.SetFont(self.themeManager.get_font('heading'))
        main_sizer.Add(priority_label, 0, wx.ALL | wx.EXPAND, 10)

        task_priority = wx.StaticText(self, label=self.task.priority.name)
        task_priority.SetFont(self.themeManager.get_font('body'))
        main_sizer.Add(task_priority, 0, wx.ALL | wx.EXPAND, 10)

        # Due Date & Time
        due_label = wx.StaticText(self, label="Due Date and Time:", style=wx.ALIGN_LEFT)
        due_label.SetFont(self.themeManager.get_font('heading'))
        main_sizer.Add(due_label, 0, wx.ALL | wx.EXPAND, 10)

        due_datetime_str = self.task.due_datetime.strftime('%Y-%m-%d %H:%M:%S')
        task_due = wx.StaticText(self, label=due_datetime_str)
        task_due.SetFont(self.themeManager.get_font('body'))
        main_sizer.Add(task_due, 0, wx.ALL | wx.EXPAND, 10)

        # Dialog Buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Close button
        close_button = wx.Button(self, label="Close")
        close_button.SetBackgroundColour(self.themeManager.get_color('button1'))
        close_button.SetForegroundColour(self.themeManager.get_color('text1'))
        close_button.SetFont(self.themeManager.get_font('button'))
        close_button.Bind(wx.EVT_BUTTON, self.on_close)

        button_sizer.Add(close_button, 0, wx.ALL | wx.CENTER, 10)

        main_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 10)

        self.SetSizer(main_sizer)
        self.Layout()

    def on_close(self, event):
        """
        Handle the close button.
        """
        self.Close()
