import wx


class TodoPanel(wx.Panel):
    def __init__(self, parent, themeManager, *args, **kwds):
        super().__init__(parent, *args, **kwds)

        self.themeManager = themeManager
        self.tasks = []  # Store tasks here

        # Set background color from theme
        self.SetBackgroundColour(self.themeManager.get_color('bg'))

        # Main vertical sizer for the panel
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Title
        title = wx.StaticText(self, label="Your To-Do List")
        title.SetFont(self.themeManager.get_font('heading'))
        title.SetForegroundColour(self.themeManager.get_color('text1'))
        main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 10)

        # Task List (wx.ListCtrl)
        self.task_list = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.task_list.InsertColumn(0, "Tasks", width=300)
        main_sizer.Add(self.task_list, 1, wx.ALL | wx.EXPAND, 10)

        # Add new task section
        add_task_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Text input for new task
        self.new_task_input = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.new_task_input.Bind(wx.EVT_TEXT_ENTER, self.add_task)  # Add task on Enter key
        add_task_sizer.Add(self.new_task_input, 1, wx.ALL | wx.EXPAND, 5)

        # Add task button
        add_task_button = wx.Button(self, label="Add Task")
        add_task_button.SetFont(self.themeManager.get_font('button'))
        add_task_button.SetBackgroundColour(self.themeManager.get_color('button1'))
        add_task_button.Bind(wx.EVT_BUTTON, self.add_task)
        add_task_sizer.Add(add_task_button, 0, wx.ALL, 5)

        # Add the new task input and button to the main sizer
        main_sizer.Add(add_task_sizer, 0, wx.ALL | wx.EXPAND, 10)

        # Set the sizer for the panel
        self.SetSizer(main_sizer)

    def add_task(self, event):
        """Add a new task to the task list."""
        new_task = self.new_task_input.GetValue().strip()
        if new_task:
            index = self.task_list.InsertItem(self.task_list.GetItemCount(), new_task)
            self.tasks.append(new_task)
            self.new_task_input.SetValue("")  # Clear the input field
        else:
            wx.MessageBox("Please enter a task.", "Error", wx.OK | wx.ICON_ERROR)
