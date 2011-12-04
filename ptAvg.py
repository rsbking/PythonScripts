#make pT total Hist
import ROOT,sys,AtlasStyle
import RatioPlot
indir = sys.argv[1]
if indir[-1]!='/': indir+='/'

f1 = ROOT.TFile(indir+"pythiaJ0muTests.root","READ")
f2 = ROOT.TFile(indir+"pythiaJ1muTests.root","READ")
f3 = ROOT.TFile(indir+"pythiaJ2muTests.root","READ")

plotName = "ptavg"

h1 = f1.Get(plotName)
h1.SetName("h1")
h1.SetColor(2)
h2 = f2.Get(plotName)
h2.SetName("h2")
h2.SetColor(3)
h3 = f3.Get(plotName)
h3.SetName("h3")
h3.SetColor(4)

hTotal = h1.Clone("hTotal")
hTotal.Add(h1)
hTotal.Add(h2)
hTotal.Add(h3)

hTotal.Draw()
h1.Draw("same")
h2.Draw("same")
h3.Draw("same")
