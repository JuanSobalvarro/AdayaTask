import os
import wx

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TASKS_PATH = os.path.join(BASE_DIR, 'tasks', 'tasks.yaml')

ICON_PATH = os.path.join(BASE_DIR, 'assets', 'icons', 'adayacropped.ico')

IMAGES_PATH = os.path.join(BASE_DIR, 'assets', 'images')

DEFAULT_THEME = 0


class ThemeManager:
    def __init__(self):
        # Define themes: 0 for Light Theme, 1 for Dark Theme
        self.current_theme = 0  # Default to light theme

        # Theme palette
        self.PALETTE = {
            'bg': ("#F7ECEB", "#"),  # White / Dark
            'primary': ("#FFBBC8", "#"),
            'secondary': ("FADEDC", (10, 10, 10)),  # Light gray / Dark gray
            'button1': ("#E0DCDB", (100, 200, 100)),
            'button2': ("#E8E5E3", (100, 200, 100)),
            'text1': ((0, 0, 0), (255, 255, 255)),  # Black text / White text
            'check1': ("#DAFF9A", "#000000"),
            'check2': ("#E8CEFF", "#000000"),
        }

        # Fonts based on the theme
        self.fonts = {
            'heading': wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD),
            'body': wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL),
            'button': wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        }

    def toggle_theme(self):
        # Toggle between 0 (light) and 1 (dark)
        self.current_theme = 1 - self.current_theme

    def get_color(self, color_name):
        # Retrieve the color for the current theme
        return self.PALETTE[color_name][self.current_theme]

    def get_font(self, font_name):
        # Retrieve the font for the current theme
        return self.fonts[font_name]
