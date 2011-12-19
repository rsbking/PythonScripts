#make a nice legend!
from ROOT import TLegend

def pLegend(xStart,yStart,xStop,yStop):
    l =  TLegend(xStart,yStart,xStop,yStop)
    l.SetFillColor(0)
    l.SetShadowColor(0)
    l.SetBorderSize(0)
    return l