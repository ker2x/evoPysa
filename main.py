"""EvoPysa : An EvoLisa Clone in Python"""

import wx
from dna.point import Point
from dna.polygon import Polygon
from dna.brush import Brush
# import os


class EvoPysa(wx.Frame):
    """Main class"""

    def __init__(self, parent, title, size=(800, 600)):
        self.fileMenu = None
        self.menuAbout = None
        self.menuBar = None
        self.menuExit = None
        self.menuOpen = None
        self.menuSave = None
        self.mainSizer = None
        self.leftSizer = None
        self.startStopButton = None
        self.scaleSlider = None

        self.frame = wx.Frame.__init__(self, parent, title=title, size=size)
        self.createMenu()
        self.createWindow()

        self.Show(True)

    def createMenu(self):
        """Setting up the menu"""
        self.fileMenu = wx.Menu()
        self.menuOpen = self.fileMenu.Append(wx.ID_OPEN, "&Open", "Open a new image")
        self.menuSave = self.fileMenu.Append(wx.ID_SAVEAS, "&Save as...", "Save a generated image")
        self.fileMenu.AppendSeparator()
        self.menuAbout = self.fileMenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        self.fileMenu.AppendSeparator()
        self.menuExit = self.fileMenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        self.Bind(wx.EVT_MENU, self.OnOpen, self.menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, self.menuSave)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, self.menuExit)

        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.fileMenu, "&File")
        self.SetMenuBar(self.menuBar)

    def createWindow(self):
        """main window"""
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.leftSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainSizer.Add(self.leftSizer, proportion=2)

        # left column
        # TODO buttons and slider should be at the bottom
        self.startStopButton = wx.Button(self, -1, "Start/Stop")
        self.scaleSlider = wx.Slider(
            self, value=1, minValue=1, maxValue=10, name="Scale",
            style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        self.leftSizer.Add(self.startStopButton, flag=wx.EXPAND, border=0)
        self.leftSizer.Add(self.scaleSlider, flag=wx.EXPAND)

        self.Bind(wx.EVT_SCROLL_CHANGED, self.OnScaleChange, self.scaleSlider)

        # right column
        # TODO remove removeme
        self.removeme = wx.Button(self, -1, "remove me")
        self.mainSizer.Add(self.removeme, proportion=8, flag=wx.EXPAND)
        self.SetSizer(self.mainSizer)

    def OnOpen(self, e):
        """Load a new image"""
        # TODO just a copypasta for now
        dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            # f = open(os.path.join(self.dirname, self.filename), 'r')
            # self.control.SetValue(f.read())
            # f.close()
        dlg.Destroy()

    def OnSave(self, e):
        """Save a generated image"""
        # TODO just a copypasta for now
        dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            # f = open(os.path.join(self.dirname, self.filename), 'r')
            # self.control.SetValue(f.read())
            # f.close()
        dlg.Destroy()

    def OnAbout(self, e):
        """A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets."""
        dlg = wx.MessageDialog(self, "A dumb EvoLisa clone as i learned wxWidget", "About EvoPysa")
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        """Close the frame"""
        self.Close(True)

    def OnScaleChange(self, e):
        """When the scale slider changed"""
        print("scale changed : ", self.scaleSlider.Value)


if __name__ == '__main__':
    print("wxPython : ", wx.version())
    p1 = Point()
    p2 = Point()
    print(p1)
    print(p2)
    app = wx.App(redirect=False, useBestVisual=True)
    evo = EvoPysa(None, "EvoPysa")
    app.MainLoop()
