import wx

from . import core
from . import gui
from . import settings


class AdayaTaskApp(wx.App):
    def __init__(self, debug=False):
        super().__init__(clearSigInt=True)
        self.debug = debug

        self.__initialize()

    def __initialize(self):
        task_manager = core.task_manager.TaskManager(settings.DB_PATH)

        if self.debug:
            print("Debug mode is ON")
            # Add any additional logging or debug-related behavior here

        main_window = gui.main_window.MainWindow(None, title='Adaya Task')
        main_window.Show()
        return True


def run(debug=False):
    app = AdayaTaskApp(debug=debug)
    app.MainLoop()
