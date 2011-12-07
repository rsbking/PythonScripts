#RatioPlot untility
#Takes two histograms as inputs and returns a canvas with a ratio plot of the two

import ROOT
from array import array

def ratioPlot(hist1,hist2,log=False,xTitle="",yTitle="",drawPlot1Opt="",drawPlot2Opt="",norm=False,ratioMin=0.5,ratioMax=1.5):
	if isinstance(hist2,list):
		if isinstance(hist1,ROOT.TGraph):
			c = multiGraphRatio(hist1,hist2,log,xTitle,yTitle,drawPlot1Opt,drawPlot2Opt,norm,ratioMin=ratioMin,ratioMax=ratioMax)
		else:
			c = multiRatio(hist1,hist2,log,xTitle,yTitle,drawPlot1Opt,drawPlot2Opt,norm,ratioMin=ratioMin,ratioMax=ratioMax)
	else:
		if isinstance(hist1,ROOT.TGraph):
			c = GraphRatio(hist1,hist2,log,xTitle,yTitle,drawPlot1Opt,drawPlot2Opt,norm,ratioMin=ratioMin,ratioMax=ratioMax)
		else:
			c = tworatios(hist1,hist2,log,xTitle,yTitle,drawPlot1Opt,drawPlot2Opt,norm,ratioMin=ratioMin,ratioMax=ratioMax)
	return c


def tworatios(hist1,hist2,log=False,xTitle="",yTitle="",drawPlot1Opt="",drawPlot2Opt="",norm=False,ratioMin=0.5,ratioMax=1.5):
	"""Takes two histograms as inputs and returns a canvas with a ratio plot of the two. 
	The two optional arguments are for the x Axis and y Axis titles"""
	
	c = makeDivCan()
	pad1 = c.cd(1)
	pad2 = c.cd(2)
	c.cd(1)
	yMax = max(hist2.GetMaximum(),hist1.GetMaximum())
	yMin = 0
	if log:
		pad1.SetLogy()
		yMin = 0.01
	
	print 'yMax is ',yMax
	try:
		hist2.GetYaxis().SetRangeUser(yMin,1.2*yMax)
	except(ReferenceError):
		h = pad1.DrawFrame(hist1.GetXaxis().GetXmin(),yMin,hist1.GetXaxis().GetXmax(),1.2*yMax)
		ROOT.SetOwnership(h,0)
	if not norm:
		#hist2.GetYaxis().SetRangeUser(0,ymax*1.2)
		hist2.Draw(drawPlot2Opt)
		hist1.Draw("same"+drawPlot1Opt)
	else:
		#hist2.GetYaxis().SetRangeUser(0,ymax*1.2)
		hist2 = hist2.DrawNormalized(drawPlot2Opt)
		hist1 = hist1.DrawNormalized("same"+drawPlot1Opt)
	ymax = max(hist1.GetMaximum(),hist2.GetMaximum())
	
	c.cd()
	c.cd(2)
	
	ratioHist = makeRatio(hist1,hist2,ymax= ratioMax,ymin=ratioMin,norm=norm)
	ROOT.SetOwnership(ratioHist,0)
	ratioHist.GetXaxis().SetTitle(xTitle)
	ratioHist.GetYaxis().SetTitle(yTitle)
	ratioHist.Draw(drawPlot1Opt)
	
	line = ROOT.TLine(ratioHist.GetXaxis().GetXmin(),1,ratioHist.GetXaxis().GetXmax(),1)
	line.SetLineStyle(2)
	line.Draw()
	ROOT.SetOwnership(line,0)
	c.cd()
	
	return c
	
def multiRatio(hist1,hist2,log=False,xTitle="",yTitle="",drawPlot1Opt="",drawPlot2Opt="",norm=False,ratioMin=0.5,ratioMax=1.5):
	"""expects a list of histograms as the second argument"""
	c = makeDivCan()
	pad1 = c.cd(1)
	pad2 = c.cd(2)
	c.cd(1)
	
	if log:
		pad1.SetLogy()
	
	maxList = []
	if not norm:
		h2[0].Draw(drawPlot2Opt)
		maxList.append(h2[0].GetMaximum())
		for h in hist2[1:]:
			h.Draw("same"+drawPlot2Opt)
			maxList.append(h.GetMaximum())
		hist1.Draw("same"+drawPlot1Opt)
		maxList.append(hist1.GetMaximum())
	else:
		h2 = hist2[0].DrawNormalized(drawPlot2Opt)
		maxList.append(h2.GetMaximum())
		for h in hist2[1:]:
			h = h.DrawNormalized("same"+drawPlot2Opt)
			maxList.append(h.GetMaximum())
		hist1 = hist1.DrawNormalized("same"+drawPlot1Opt)
		maxList.append(hist1.GetMaximum())
	ymax = max(*maxList)
	h2.GetYaxis().SetRangeUser(0,ymax*1.2)
	c.cd()
	c.cd(2)
	ratios = []
	
	ratioHist = makeRatio(hist1,hist2[0],ymax= ratioMax,ymin=ratioMin,norm=norm)
	ROOT.SetOwnership(ratioHist,0)
	ratioHist.GetXaxis().SetTitle(xTitle)
	ratioHist.GetYaxis().SetTitle(yTitle)
	
	
	ratioHist.SetLineColor(hist2[0].GetLineColor())
	ratioHist.Draw(drawPlot1Opt)
	
	for h in hist2[1:]:
		ratioHist = makeRatio(hist1,h,ymax= ratioMax,ymin=ratioMin,norm=norm)
		ROOT.SetOwnership(ratioHist,0)
		ratioHist.GetXaxis().SetTitle(xTitle)
		ratioHist.GetYaxis().SetTitle(yTitle)
		
		ratioHist.SetLineColor(h.GetLineColor())
		ratioHist.Draw(drawPlot1Opt+"SAME")
	
	line = ROOT.TLine(ratioHist.GetXaxis().GetXmin(),1,ratioHist.GetXaxis().GetXmax(),1)
	line.SetLineStyle(2)
	line.Draw()
	ROOT.SetOwnership(line,0)
	c.cd()
	
	return c
	
	
def makeRatio(hist1,hist2,ymax=False,ymin=False,norm=False):
	"""returns the ratio plot hist2/hist1
	if one of the histograms is a stack put it in as argument 2!"""
	
	if norm:
		print 'scaling!'
		try:
			print 'scale 1: ',1/hist1.Integral()
			print 'scale 2: ',1/hist2.Integral()
			hist1.Scale(1/hist1.Integral())
			hist2.Scale(1/hist2.Integral())
		except(ZeroDivisionError):
			pass
	retH = hist1.Clone()
	try:
		retH.Divide(hist2)
	except(TypeError):
		#this is the error you get if hist2 is a stack
		hList = hist2.GetHists()
		sumHist = hist1.Clone("sumHist")
		sumHist.Reset()
		for h in hList:
			sumHist.Add(h)
		retH.Divide(sumHist)
	except(AttributeError):
		#this is the error you get if hist1 is a stack
		print "Did you use a stack as argument 1? please use stack as argument 2!"
		raise AttributeError
	if ymax or ymin:
		retH.GetYaxis().SetRangeUser(ymin,ymax)
	ROOT.SetOwnership(retH,0)
	return retH
	
	
def makeDivCan():
	"""returns a divided canvas for ratios"""
	Rcanv = ROOT.TCanvas("Rcanv","Rcanv",1024,768)
	Rcanv.cd()
	pad1 = ROOT.TPad("pad1","pad1",0,0.3,1,1)
	pad1.SetNumber(1)
	pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.3)
	pad2.SetNumber(2)
	
	pad1.Draw()
	pad2.Draw()
	Rcanv.cd()
	#ROOT.SetOwnership(Rcanv,0)
	ROOT.SetOwnership(pad1,0)
	ROOT.SetOwnership(pad2,0)
	#print "check stuff", canv.GetPad(1)
	return Rcanv
	

	
def MakeStatProgression(myHisto,title=""):
	"""This function returns a function with the statistical precision in each bin"""
	statPrecision = myHisto.Clone()
	##statPrecision.Reset()
	statPrecision.SetTitle(title)
	for bin in range(myHisto.GetNbinsX()):
		y=statPrecision.GetBinContent(bin);
		err=statPrecision.GetBinError(bin);
		if (y>0): statPrecision.SetBinContent(bin,err/y);
		statPrecision.SetBinError(bin,0);
		
	return statPrecision
	

#######################################################################
##Now for graphs!!
###########################################



def MakeRatioGraphs(array1,array2,xMin,xMax,yMin,yMax):
	"""make ratio graphs from arrays"""
	c = makeDivCan()
	c.cd(1)
	if xMin:
		c.DrawFrame(xMin,yMin,xMax,yMax)
	
	g1 = ROOT.TGraph(len(array1[0]),*array1)
	
	g2 = ROOT.TGraph(len(array1[0]),*array2)
	
def GraphRatio(array1,array2):
	"""takes two arrays that are made to make graphs and return one array which is for the ratio of the two"""
	x = array("d",[]) 
	y = array("d",[])
	xer = array("d",[])
	yer = array("d",[])
	for (i,x1) in enumerate(array1[0]):
		if x1 not in array2[0]: continue # if the point x1 isn't in the second array then we don't want anything for this point
		i2 = 0
		for (j,x2) in enumerate(array2[0]):
			if x2==x1:
				i2=j
				break
		x.append(x1)
		
		yR = array1[1][i]/array2[1][i2]
		y.append(yR)
		xRer = array1[2][i]
		xer.append(xRer)
		yRer = ROOT.TMath.Sqrt(array1[3][i]*array1[3][i] + array2[3][i2]*array2[3][i2])
		yer.append(yRer)
		
	return [x,y,xer,yer]
		