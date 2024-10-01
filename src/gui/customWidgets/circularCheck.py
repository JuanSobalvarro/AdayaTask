import wx
import wx.lib.newevent

class CircularCheckBox(wx.Panel):
    """Custom circular checkbox."""
    def __init__(self, parent, radius, check_proportion=0.7, bg_color="#FFFFFF", inner_bg_color="#FFFFFF", check_color="#000000", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.checked = False
        self.radius = radius  # Define the radius of the circular checkbox
        self.check_proportion = check_proportion
        self.bg_color = bg_color
        self.inner_bg_color = inner_bg_color
        self.check_color = check_color

        self.border1 = 2
        self.border2 = 2

        # Set minimum size for the panel to ensure it has enough space for the circle
        self.SetMinSize((self.radius * 2 + self.border1 * 2, self.radius * 2 + self.border1 * 2))  # Add padding

        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_click)

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)

        # Clear the background
        dc.SetBackground(wx.Brush(wx.Colour(self.bg_color)))
        # dc.SetBackground(wx.Brush('white'))
        dc.Clear()  # This is the method to clear the background

        # Draw the circle outline
        gc.SetPen(wx.Pen(wx.Colour("#979797"), self.border1))  # Black border
        gc.SetBrush(wx.Brush(wx.Colour(self.inner_bg_color)))  # White background

        # Draw the outer circle
        # Since our border is 2 we should draw with a padding of 2
        gc.DrawEllipse(self.border1 / 2, self.border1 / 2, self.radius * 2 + self.border1, self.radius * 2 + self.border1)

        # If checked, draw the inner circle
        if self.checked:
            gc.SetPen(wx.Pen(wx.Colour(self.check_color), self.border2))
            gc.SetBrush(wx.Brush(wx.Colour(self.check_color)))  # Green check color
            values = self.__calculateInnerCircleCoords(self.check_proportion)
            gc.DrawEllipse(values[0], values[0], values[1], values[1])

    def on_click(self, event):
        self.checked = not self.checked
        self.Refresh()  # Repaint after the click

    def is_checked(self):
        return self.checked

    def __calculateInnerCircleCoords(self, proportion: float) -> tuple[int, float]:
        """
        This method calculates the ellipse coords for the inner circle given a proportion
        """
        padding = self.radius + self.border1 - self.radius * proportion - self.border2 / 2
        corner = 2 * self.radius * proportion + self.border2
        return padding, corner


