import wx
import wx.grid
from .. import settings
from . import todo_panel
from . import menu_panel
from . import settings_panel
from ..core.task_manager import TaskManager
from ..core.theme_manager import ThemeManager


class MainWindow(wx.Frame):
    def __init__(self, task_manager: TaskManager, theme_manager: ThemeManager, *args, **kwds):
        super().__init__(*args, **kwds)
        self.SetSize(480, 480)
        self.SetIcon(wx.Icon(settings.load_settings()['icon_path']))
        self.current_panel = None
        self.panel_stack = []  # Stack to track previous panels

        self.themeManager: ThemeManager = theme_manager
        self.taskManager: TaskManager = task_manager

        # Create a sizer to manage the layout of panels
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.main_sizer)

        # Call to the function which shows the menu Panel
        self.showMenuPanel()

    def showPanel(self, panel_class, add_to_stack=True):
        """Display a panel and manage navigation."""
        if self.current_panel:
            if add_to_stack:
                # Hide the current panel and add it to the stack
                self.panel_stack.append(type(self.current_panel))  # Add current panel class to stack
                self.current_panel.Destroy()  # Destroy the current panel
                self.current_panel = None

        # Create the new panel
        self.current_panel = panel_class(self, self.themeManager, self.taskManager)
        self.main_sizer.Add(self.current_panel, 1, wx.EXPAND)  # Add the new panel to the sizer

        self.current_panel.Show()
        self.Layout()  # Refresh layout

    def update_current_panel(self):
        """Recreate the current panel to reflect the updated theme."""
        if self.current_panel:
            panel_class = type(self.current_panel)  # Get the current panel class
            self.showPanel(panel_class, add_to_stack=False)  # Recreate it

    def update_all_panels(self):
        """Recreate all panels in the stack to reflect the updated theme."""
        # Create a temporary stack to hold the panel classes
        temp_stack = []

        # First, update the current panel if it exists
        if self.current_panel:
            temp_stack.append(type(self.current_panel))
            self.current_panel.Destroy()  # Destroy current panel

        # Now, iterate through the panel stack to recreate each panel
        while self.panel_stack:
            panel_class = self.panel_stack.pop()
            temp_stack.append(panel_class)  # Keep track of panel classes

        # Recreate panels in the same order
        for panel_class in reversed(temp_stack):
            self.showPanel(panel_class, add_to_stack=False)

    def showMenuPanel(self):
        """Show the menu panel."""
        self.showPanel(menu_panel.MenuPanel, add_to_stack=True)

    def showSettingsPanel(self):
        """Show the settings panel."""
        self.showPanel(settings_panel.SettingsPanel)

    def showTodoPanel(self):
        """Show the task management panel."""
        self.showPanel(todo_panel.TodoPanel)

    def navigateBack(self):
        """Navigate back to the previous panel."""
        if self.panel_stack:
            # Hide the current panel and bring back the previous one
            self.current_panel.Destroy()  # Destroy current panel
            prev_panel_class = self.panel_stack.pop()  # Get the previous panel class
            self.showPanel(prev_panel_class, add_to_stack=False)  # Show the previous panel
        else:
            wx.MessageBox("No previous panel to go back to.", "Navigation Error", wx.OK | wx.ICON_INFORMATION)

    def OnClose(self, event):
        dialog = wx.MessageDialog(self, "Do you really want to close the application?",
                                  "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)

        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
