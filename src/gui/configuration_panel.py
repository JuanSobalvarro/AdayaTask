import wx


class ConfigurationPanel(wx.Panel):
    def __init__(self, parent, themeManager):
        super().__init__(parent, themeManager)

        self.themeManager = themeManager

        self.SetBackgroundColour(self.themeManager.get_color('bg_color'))

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Add some settings elements (e.g., checkbox for dark mode)
        dark_mode_checkbox = wx.CheckBox(self, label="Enable Dark Mode")
        vbox.Add(dark_mode_checkbox, 0, wx.ALL, 10)

        self.SetSizer(vbox)

        # Bind events
        dark_mode_checkbox.Bind(wx.EVT_CHECKBOX, self.on_toggle_dark_mode)

    def on_toggle_dark_mode(self, event):
        # Logic to handle dark mode toggle
        print("Dark Mode toggled!")
