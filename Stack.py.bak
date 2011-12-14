#this file contains methods for making nice stacks:
import ROOT
def histCompare(histogram1,histogram2):
	"""This function defines how to compare histograms. 
	Returns negative if histogram1<histogram2, +ve if histogram1>histogram2 and zero otherwise"""
	integral1 = histogram1.Integral()
	integral2 = histogram2.Integral()
	diff = integral1 - integral2
	if diff > 0: return 1
	if diff < 0: return -1
	else: return 0
	
def sortHistograms(histoList):
	"""This function takes a list of histograms and returns a list sorted with smallest first"""
	newHistoList = sorted(histoList, cmp=histCompare)
	return newHistoList
	
def makeTHStack(histoList,secondaryList=[],stackTitle="defaultStack"):
	"""This function takes a list of backgrounds and adds them to the THStack.
	If a secondary List is provided then these are added at the end to allow 'signal' to be ontop of everything else"""
	print "in makeTHStack"
	sortedHistos = sortHistograms(histoList)
	print "histograms sorted"
	newStack = ROOT.THStack(stackTitle,stackTitle)
	print "stack created"
	for h in sortedHistos:
		#print "fill color is ",h.GetFillColor()
		newStack.Add(h)
	print "First list added"
	for h in secondaryList:
		newStack.Add(h)
	print "second list added"
	print "type newStack ", newStack
	#newStack.Draw()
	ROOT.SetOwnership(newStack,0)
	return newStack