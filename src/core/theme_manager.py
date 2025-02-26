import wx
from .. import settings


class ThemeManager:
    def __init__(self):
        # Define themes: 0 for Light Theme, 1 for Dark Theme
        self.current_theme = settings.load_settings()['theme']

        # Theme palette
        self.PALETTE = {
            'bg': ("#F7ECEB", "#2B2B2B"),  # Light background / Dark background
            'primary': ("#FFBBC8", "#3A3A3A"),
            'secondary': ("#FADEDC", "#4F4F4F"),  # Light gray / Dark gray
            'button1': ("#E0DCDB", "#5A5A5A"),
            'button2': ("#E8E5E3", "#6A6A6A"),
            'text1': ((0, 0, 0), (255, 255, 255)),  # Black text / White text
            'check1': ("#3FA7D6", "#FFCE00"),
            'check2': ("#E8CEFF", "#00FFCE"),
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

    def set_theme(self, theme: int):
        """
        To set theme 0 is light and 1 is dark
        """
        if theme == 0 or theme == 1:
            self.current_theme = theme

    def get_color(self, color_name):
        # Retrieve the color for the current theme
        return self.PALETTE[color_name][self.current_theme]

    def get_font(self, font_name):
        # Retrieve the font for the current theme
        return self.fonts[font_name]

    def apply_theme(self, frame):
        """
        Apply the current theme to the entire application window (frame).

        Parameters:
        - frame (wx.Frame): The main frame of the application.
        """
        # Set the background color for the frame
        frame.SetBackgroundColour(self.get_color('bg'))

        # Apply theme to all child widgets of the frame
        for child in frame.GetChildren():
            self.apply_theme_to_widget(child)

        # Refresh the frame to apply changes
        frame.Refresh()

    def apply_theme_to_widget(self, widget):
        """
        Apply theme to an individual widget and its children.

        Parameters:
        - widget (wx.Window): The widget to apply the theme to.
        """
        # Apply background and text color
        if isinstance(widget, wx.Panel):
            widget.SetBackgroundColour(self.get_color('primary'))

        elif isinstance(widget, wx.StaticText):
            widget.SetForegroundColour(self.get_color('text1'))

        elif isinstance(widget, wx.Button):
            widget.SetBackgroundColour(self.get_color('button1'))
            widget.SetForegroundColour(self.get_color('text1'))
            widget.SetFont(self.get_font('button'))

        # Recursively apply theme to all children of the widget
        for child in widget.GetChildren():
            self.apply_theme_to_widget(child)

        # Refresh the widget to apply changes
        widget.Refresh()
