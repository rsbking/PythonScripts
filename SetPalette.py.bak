from array import array
from ROOT import gStyle, TColor

class SetPalette:
    __shared_state = {}
    first = 1
    def __init__(self):
        self.__dict__ = self.__shared_state
        if self.first:
            print "Setting Palette"
            self.set_palette()
            self.first = 0

    def set_palette(name='palette', ncontours=999):
        """Set a color palette from a given RGB list
        stops, red, green and blue should all be lists of the same length
        see set_decent_colors for an example"""

        if name == "gray" or name == "grayscale":
            stops = [0.00, 0.34, 0.61, 0.84, 1.00]
            red   = [1.00, 0.84, 0.61, 0.34, 0.00]
            green = [1.00, 0.84, 0.61, 0.34, 0.00]
            blue  = [1.00, 0.84, 0.61, 0.34, 0.00]
            # elif name == "whatever":
                # (define more palettes)
        else:
            # default palette, looks cool
            stops = [0.00, 0.34, 0.61, 0.84, 1.00]
            red   = [0.00, 0.00, 0.87, 1.00, 0.51]
            green = [0.00, 0.81, 1.00, 0.20, 0.00]
            blue  = [0.51, 1.00, 0.12, 0.00, 0.00]

        s = array('d', stops)
        r = array('d', red)
        g = array('d', green)
        b = array('d', blue)

        npoints = len(s)
        TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
        gStyle.SetNumberContours(ncontours)

