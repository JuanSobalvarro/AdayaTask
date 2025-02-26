import wx


class BasePanel(wx.Panel):
    def __init__(self, parent, themeManager, taskManager, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.themeManager = themeManager
        self.taskManager = taskManager

        # Optional: You can define a main sizer for common layout purposes
        # self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        # self.SetSizer(self.main_sizer)

    def add_navigation(self, panel_sizer):
        """Optional method to handle adding navigation buttons like Back button."""
        self.back_button = wx.Button(self, label="Back")
        self.back_button.Bind(wx.EVT_BUTTON, self.on_back)
        panel_sizer.Add(self.back_button, 0, wx.ALL | wx.ALIGN_LEFT, 10)

    def on_back(self, event):
        """Default behavior for back navigation"""
        parent_frame = self.GetParent()
        if hasattr(parent_frame, 'navigate_back'):
            parent_frame.navigateBack()
        else:
            wx.MessageBox("No back navigation defined!", "Error", wx.OK | wx.ICON_ERROR)
