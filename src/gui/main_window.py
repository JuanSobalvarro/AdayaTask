import wx
import wx.grid
from .. import settings
from . import todo_panel as todo
from . import menu_panel as menu
from . import configuration_panel as configuration
from ..core.task_manager import TaskManager
from ..core.theme_manager import ThemeManager


class MainWindow(wx.Frame):
    def __init__(self, task_manager: TaskManager, theme_manager: ThemeManager, *args, **kwds):
        super().__init__(*args, **kwds)
        self.SetSize(480, 480)
        self.SetIcon(wx.Icon(settings.ICON_PATH))
        # self.SetBackgroundColour(wx.BLACK)
        self.current_panel = None

        self.themeManager: ThemeManager = theme_manager
        self.taskManager: TaskManager = task_manager

        # Call to the function which shows the menu Panel
        self.showMenuPanel()

        # self.Bind(wx.EVT_CLOSE, self.OnClose)

    def showMenuPanel(self):
        panel = menu.MenuPanel(self, self.themeManager)
        self.switchPanel(panel)

    def showTodoPanel(self):
        panel = todo.TodoPanel(self, self.themeManager, self.taskManager)
        self.switchPanel(panel)

    def showSettingsPanel(self):
        panel = configuration.ConfigurationPanel(self, self.themeManager)
        self.switchPanel(panel)

    def switchPanel(self, new_panel):
        if self.current_panel:
            self.current_panel.Destroy()

        self.current_panel = new_panel
        self.current_panel.Show()

        self.Layout()

    def OnClose(self, event):
        dialog = wx.MessageDialog(self, "Do you really want to close the application?",
                                  "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)

        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
