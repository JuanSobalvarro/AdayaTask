import wx

from .customWidgets.basePanel import BasePanel
from ..settings import load_settings, save_settings, DEFAULT_SETTINGS
from ..core.theme_manager import ThemeManager  # Import your theme manager function


class SettingsPanel(BasePanel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.settings = load_settings()

        # Set background color
        self.SetBackgroundColour(self.themeManager.get_color('bg'))

        # Create UI Elements
        theme_label = wx.StaticText(self, label="Theme:")
        self.theme_choice = wx.Choice(self, choices=["Light", "Dark"])
        self.theme_choice.SetSelection(self.settings.get('theme', 0))

        tasks_path_label = wx.StaticText(self, label="Tasks File Path:")
        self.tasks_path_picker = wx.FilePickerCtrl(self, path=self.settings.get('tasks_path'))

        icon_path_label = wx.StaticText(self, label="Icon Path:")
        self.icon_path_picker = wx.FilePickerCtrl(self, path=self.settings.get('icon_path'))

        images_path_label = wx.StaticText(self, label="Images Folder Path:")
        self.images_path_picker = wx.DirPickerCtrl(self, path=self.settings.get('images_path'))

        # Buttons
        apply_button = wx.Button(self, label="Apply")
        reset_button = wx.Button(self, label="Reset to Defaults")
        self.back_button = wx.Button(self, label="Back")

        # Set button colors
        apply_button.SetBackgroundColour(self.themeManager.get_color('button1'))
        reset_button.SetBackgroundColour(self.themeManager.get_color('button1'))
        self.back_button.SetBackgroundColour(self.themeManager.get_color('button1'))

        apply_button.SetForegroundColour(self.themeManager.get_color('text1'))
        reset_button.SetForegroundColour(self.themeManager.get_color('text1'))
        self.back_button.SetForegroundColour(self.themeManager.get_color('text1'))

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(theme_label, 0, wx.ALL, 5)
        sizer.Add(self.theme_choice, 0, wx.ALL, 5)
        sizer.Add(tasks_path_label, 0, wx.ALL, 5)
        sizer.Add(self.tasks_path_picker, 0, wx.ALL, 5)
        sizer.Add(icon_path_label, 0, wx.ALL, 5)
        sizer.Add(self.icon_path_picker, 0, wx.ALL, 5)
        sizer.Add(images_path_label, 0, wx.ALL, 5)
        sizer.Add(self.images_path_picker, 0, wx.ALL, 5)

        # Buttons Layout
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(apply_button, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        button_sizer.Add(reset_button, 0, wx.ALL | wx.ALIGN_LEFT, 5)
        button_sizer.Add(self.back_button, 0, wx.ALL | wx.ALIGN_LEFT, 5)

        sizer.Add(button_sizer, 0, wx.ALIGN_CENTER)

        self.SetSizer(sizer)

        # Bind Events
        apply_button.Bind(wx.EVT_BUTTON, self.on_apply)
        reset_button.Bind(wx.EVT_BUTTON, self.on_reset)
        self.back_button.Bind(wx.EVT_BUTTON, self.on_back)

    def on_apply(self, event):
        # Update settings
        self.settings['theme'] = self.theme_choice.GetSelection()
        self.settings['tasks_path'] = self.tasks_path_picker.GetPath()
        self.settings['icon_path'] = self.icon_path_picker.GetPath()
        self.settings['images_path'] = self.images_path_picker.GetPath()

        # Apply the selected theme
        self.themeManager.set_theme(self.settings['theme'])

        self.Parent.update_all_panels()

        # Save settings to file
        save_settings(self.settings)
        wx.MessageBox("Settings have been applied!", "Success", wx.OK | wx.ICON_INFORMATION)

    def on_reset(self, event):
        # Reset to default settings
        self.settings = DEFAULT_SETTINGS
        self.theme_choice.SetSelection(self.settings['theme'])
        self.tasks_path_picker.SetPath(self.settings['tasks_path'])
        self.icon_path_picker.SetPath(self.settings['icon_path'])
        self.images_path_picker.SetPath(self.settings['images_path'])

        # Apply default theme
        self.themeManager.set_theme(self.settings['theme'])

        wx.MessageBox("Settings have been reset to defaults.", "Reset", wx.OK | wx.ICON_INFORMATION)

    def on_back(self, event):
        """Method to handle back navigation."""
        self.Parent.navigateBack()  # Call navigateBack from MainWindow
