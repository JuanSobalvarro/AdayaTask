import wx
import os
from .. import settings


class MenuPanel(wx.Panel):
    def __init__(self, parent, themeManager):
        super().__init__(parent)

        self.parent = parent

        self.themeManager = themeManager

        # Create a vertical box sizer to arrange elements vertically
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.__build()

    def __build(self):
        self.__addAdayaImage()

        self.SetBackgroundColour(self.themeManager.get_color('bg'))

        # Welcome message with varied font styles
        welcome_text = wx.StaticText(self, label="Welcome! I am Adaya,\nyour task manager.")
        welcome_text.SetFont(self.themeManager.get_font('heading'))
        self.sizer.Add(welcome_text, 0, wx.ALL | wx.CENTER, 20)

        # Button to go to the To-Do List panel
        todo_button = wx.Button(self, label="To-Do List")
        todo_button.SetForegroundColour(self.themeManager.get_color('text1'))
        todo_button.SetBackgroundColour(self.themeManager.get_color('button1'))
        todo_button.SetFont(self.themeManager.get_font('button'))  # Bold button text
        self.sizer.Add(todo_button, 0, wx.ALL | wx.CENTER, 10)

        # Button to go to the settings panel
        settings_button = wx.Button(self, label="Settings")
        settings_button.SetForegroundColour(self.themeManager.get_color('text1'))
        settings_button.SetBackgroundColour(self.themeManager.get_color('button1'))
        settings_button.SetFont(self.themeManager.get_font('button'))  # Bold button text
        self.sizer.Add(settings_button, 0, wx.ALL | wx.CENTER, 10)

        # Add another spacer at the bottom to balance the layout
        self.sizer.AddStretchSpacer()

        # Set the sizer for this panel
        self.SetSizer(self.sizer)

        # Bind button events
        todo_button.Bind(wx.EVT_BUTTON, lambda evt: self.parent.showTodoPanel())
        settings_button.Bind(wx.EVT_BUTTON, lambda evt: self.parent.showSettingsPanel())

    def __addAdayaImage(self):
        # Add the Adaya image to the panel
        adaya_image_path = os.path.join(settings.IMAGES_PATH, 'adayacropped.png')
        if os.path.exists(adaya_image_path):
            image = wx.Image(adaya_image_path, wx.BITMAP_TYPE_ANY)
            image = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
            bitmap = wx.StaticBitmap(self, -1, wx.Bitmap(image))

            self.sizer.Add(bitmap, 0, wx.ALL | wx.CENTER, 10)