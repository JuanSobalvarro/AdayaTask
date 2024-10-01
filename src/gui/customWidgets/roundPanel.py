import wx


class RoundPanel(wx.Panel):
    def __init__(self, parent, radius: int, bg_color: str = "#FFFFFF", inner_bg_color: str = "#FFFFFF",
                 border: int = 0, border_color: str = "#000000", *args, **kwds):
        super().__init__(parent=parent, *args, **kwds)
        self.border = border
        self.border_color = border_color
        self.radius = radius
        self.bg_color = bg_color
        self.inner_bg_color = inner_bg_color

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        gc = wx.GCDC(dc)
        gc.Clear()

        dc.SetBackground(wx.Brush(self.bg_color))
        dc.Clear()


        width, height = self.GetSize()

        if self.border != 0:
            gc.SetPen(wx.Pen(wx.Colour(self.border_color), self.border))
        else:
            gc.SetPen(wx.Pen(wx.Colour(self.inner_bg_color), self.border))
        gc.SetBrush(wx.Brush(self.inner_bg_color))

        gc.DrawRoundedRectangle(0, 0, width, height, self.radius)

    def OnSize(self, event):
        self.Refresh()  # Redraw the panel whenever resized
        event.Skip()