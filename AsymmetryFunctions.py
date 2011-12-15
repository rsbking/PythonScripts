#This contains some common functions used in several macros
import ROOT
from array import array
from random import random
from math import sqrt

def SetStyle(batchSwitch=1):
    import atlasStyle
    ROOT.gROOT.ForceStyle()
    ROOT.gROOT.SetStyle("Plain")
    ROOT.gROOT.LoadMacro("/home/king/Physics/atlasstyle-00-03-04/AtlasStyle.C")
    #ROOT
    ROOT.gROOT.SetBatch(batchSwitch)
    ROOT.gStyle.SetOptStat(01)


def EMtoLC(theName):
    """This function takes one argument, a name, and replaces 'TopoEM' with 'LCTopo' """
    rValue =  theName.replace("TopoEM","LCTopo")
    return rValue

def SetUpPoint(hist,graph,bin,EtaBins):
    """This function takes the bins from one histogram and fills a graph with them"""
    Entries = hist.GetBinEntries(bin+1)

    if Entries <1:
        return
        #don't set point if no entries doesn't mean anything
    AsymAv = hist.GetBinContent(bin+1)
    AsymEr = hist.GetBinError(bin+1)
    R = (2+AsymAv)/(2-AsymAv) #=1/c
    Rer = ROOT.TMath.Sqrt((AsymEr/2-AsymAv)*(AsymEr/2-AsymAv) + (AsymEr/2+AsymAv)*(AsymEr/2+AsymAv) )
    etaRange = float(EtaBins[bin+1]) - float(EtaBins[bin])
    etaMidPoint = float(EtaBins[bin]) + etaRange/2

    graph.SetPoint(bin,etaMidPoint,R)
    graph.SetPointError(bin,etaRange/2,Rer/2)
    #add this to allow ratio plot
    #print "[R,Rer/2,etaMidPoint,etaRange] = ",R,Rer/2,etaMidPoint,etaRange
    return [R,Rer/2,etaMidPoint,etaRange]

def ReturnArraysHist(hist,graphN,EtaBins):
    """Return a list of arrays of x,y,erx,ery
    The errors are calculated so that it uses the number of actual entries rather than effective entries.
    """
    #import cPickle
    x =array("d",[])
    y = array("d",[])
    xer = array("d",[])
    yer = array("d",[])
    for bin in range(graphN):
        Entries = hist.GetBinEntries(bin+1)
        if Entries <1:
            continue
        AsymAv = hist.GetBinContent(bin+1)
        Error = hist.GetBinError(bin+1)
        #recalculate errors:
        #this is on the basis that the error from
        #getBinError is RMS/Sqrt(Neff) and we actually
        #want RMS/Sqrt(N)
        sqrN = ROOT.TMath.Sqrt( hist.GetBinEntries(bin+1) )
        sqrNeff = ROOT.TMath.Sqrt( hist.GetBinEffectiveEntries(bin+1) )
        AsymEr = Error * (sqrNeff/sqrN)

        R = (2+AsymAv)/(2-AsymAv) #=1/c
        RerFrac = ROOT.TMath.Sqrt((AsymEr/(2-AsymAv))*(AsymEr/(2-AsymAv)) + (AsymEr/(2+AsymAv))*(AsymEr/(2+AsymAv)) )
        Rer = RerFrac * R #this fixed 21-7-11 think this should fix my errors.

        etaRange = float(EtaBins[bin+1]) - float(EtaBins[bin])
        etaMidPoint = float(EtaBins[bin]) + etaRange/2
        x.append(etaMidPoint)
        y.append(R)
        xer.append(etaRange/2)
        yer.append(Rer)

    returnList = [x,y,xer,yer]
    #histname = hist.GetName()
    #outputFile = open(histname+"array.pkl","w")
    #cPickle.dump(returnList,outputFile)

    return returnList

def ReturnArraysHistAddBins(hist,graphN,EtaBins,nAdd = 2):
    hist.Rebin(nAdd)
    wideEtaBins = []
    for i,bin in enumerate(EtaBins):
        if i%2 !=0:
            continue
        wideEtaBins.append(bin)
    nBins = len(wideEtaBins) - 1
    return ReturnArraysHist(hist,nBins,wideEtaBins)


def ReturnArrays2DHist(hist2d,graphN,EtaBins):
    """This function takes as input a 2d histogram, turns it into a set of arrays to make a TGraphErrors. Doing this in the function allows you to find the """
    profile = hist2d.ProfileX()
    #note this doesn't work yet...

def ReturnArraysHistDoubleBins(hist,graphN,EtaBins):
    """Return a list of arrays of x,y,erx,ery, combining so that the binning is reduced by half"""

    #make an array of the Nentries for each bin so that they can be weighted
    eArr = []
    Nbins = hist.GetNbinsX()
    for b in range(Nbins):
        entries = hist.GetBinEntries(b+1)
        eArr.append(entries)

    narrowBins = ReturnArraysHist(hist, graphN, EtaBins)
    #now combine adjoining bins:
    x = narrowBins[0]
    y = narrowBins[1]
    xer = narrowBins[2]
    yer = narrowBins[3]

    widex = array("d",[])
    widey = array("d",[])
    widexer = array("d",[])
    wideyer = array("d",[])
    if len(x) != len(eArr):
        print "Achtung! something fishy!"
        import sys
        sys.exit()
    for i in range(len(x)):
        if i%2 > 0:
            continue #only do for every other bin

        try:
            xcomb = (x[i] + x[i+1])/(2) #x position is just mid point
            #y position is weighted average
            ycomb = (y[i]*eArr[i] + y[i+1]*eArr[i+1])/(eArr[i] + eArr[i+1])
            xercomb = xer[i] + xer[i+1] #x error is straight sum
            yercomb = (yer[i]*eArr[i] + yer[i+1]*eArr[i+1])/(eArr[i] + eArr[i+1])
        except(ZeroDivisionError):
            xcomb, ycomb, xercomb

        widex.append(xcomb)
        widey.append(ycomb)
        widexer.append(xercomb)
        wideyer.append(yercomb)

    return [widex,widey,widexer,wideyer]

def GeterrorDef1(AsymEr,AsymAv):
    """Old definition of errors. This is probably wrong"""
    return sqrt((AsymEr/(2-AsymAv))*(AsymEr/(2-AsymAv)) + (AsymEr/(2+AsymAv))*(AsymEr/(2+AsymAv)) )
    
def GeterrorDef2(AsymEr,AsymAv):
    """New definition of errors, this is correct I think"""
    return (4*AsymEr/((2 - AsymAv)**2))

def ReturnArray2dProf(hist,EtaBins,xBin):
    """Return a list of arrays of x,y,erx,ery"""
    x = array("d",[])
    y = array("d",[])
    xer = array("d",[])
    yer = array("d",[])
    nEtaBins = len(EtaBins) - 1
    for yBin in range(nEtaBins):
        globalBin = hist.GetBin(xBin+1,yBin+1)
        #get the global bin number so can call it with just one number
        #remember! bin zero is underflow!
        Entries = hist.GetBinEntries(globalBin)
        if Entries <1:
            continue
        AsymAv = hist.GetBinContent(globalBin)
        AsymEr = hist.GetBinError(globalBin )
        R = (2+AsymAv)/(2-AsymAv) #=1/c
        Rer = GeterrorDef2(AsymEr,AsymAv)
        etaRange = float(EtaBins[bin+1]) - float(EtaBins[bin])
        etaMidPoint = float(EtaBins[bin]) + etaRange/2
        x.append(etaMidPoint)
        y.append(R)
        xer.append(etaRange/2)
        yer.append(Rer)

    return [x,y,xer,yer]

def GetArraysFromProfiles(prof):
    """reutrn a list of arrays of x,y,erx,ery"""
    x = array("d",[])
    y = array("d",[])
    xer = array("d",[])
    yer = array("d",[])
    nEtaBins = prof.GetNbinsX()
    for yBin in range(nEtaBins):
        currentBin = yBin+1
        if currentBin>nEtaBins: print "actung, bin number ",currentBin
        entries = prof.GetBinEntries(currentBin)
        if entries == 0  : continue #don't fill for this binning
        AsymAv = prof.GetBinContent(currentBin)
        AsymEr = prof.GetBinError(currentBin)
        R = (2+AsymAv)/(2-AsymAv) #=1/c
        Rer = GeterrorDef2(AsymEr,AsymAv)

        etaRange = prof.GetBinLowEdge(currentBin+1) - prof.GetBinLowEdge(currentBin)
        etaMidPoint = prof.GetBinCenter(currentBin)
        x.append(etaMidPoint)
        y.append(R)
        xer.append(etaRange/2)
        yer.append(Rer)
    return [x,y,xer,yer]

def GetArraysFromHists(hist1,hist2=None):
    """This takes two histograms and returns an array to make TGraphErrors
    the first is the weighted version, the second is the unweighted (optional)
    if the second is provided it will be used to calculate the errors"""
    #
    
    profW = hist1.ProfileX(str(random()))
    arrayW = GetArraysFromProfiles(profW)
    if not hist2:
        return arrayW
    #if we do have hist2 we use it to calculate the errors:
    profUW = hist2.ProfileX(str(random()))
    print profUW
    arrayUW = GetArraysFromProfiles(profUW)
    return [arrayW[0],arrayW[1],arrayUW[2],arrayUW[3]]
        
def GetArraysFromHistsTest(hist1,hist2=None):
    
    #if we do have hist2 we use it to calculate the errors:
    x = array("d",[])
    y = array("d",[])
    xer = array("d",[])
    yer = array("d",[])
    for b in range(hist1.GetNbinsX()):
        hTMP = hist1.ProjectionY("weightedHist"+str(random()),b+1,b+1,'e')
        if hist2:
            hUW = hist2.ProjectionY("UWHist"+str(random()),b+1,b+1,'e')
        else:
            hUW = hTMP
        rms = hTMP.GetRMS()
        Nent = hUW.GetEffectiveEntries()
        try:
            AsymEr = rms/ROOT.TMath.Sqrt(Nent)
        except(ZeroDivisionError):
            continue
        AsymAv = hTMP.GetMean()
        R = (2+AsymAv)/(2-AsymAv)
        t1 = AsymEr/(2-AsymAv)
        gerror = GeterrorDef2(AsymEr,AsymAv)
        etaRange = hist1.GetXaxis().GetBinUpEdge(b+1) - hist1.GetXaxis().GetBinLowEdge(b+1) 
        etaMidPoint = hist1.GetXaxis().GetBinCenter(b+1)
        x.append(etaMidPoint)
        xer.append(etaRange/2)
        y.append(R)
        yer.append(gerror)
    return [x,y,xer,yer]

def BiggestHisto(hlist,rootFile):

    """This function takes a list of histogram names and a root file that contains them and returns the one with the most entries"""

    rf = ROOT.TFile(rootFile)
    emax = 0
    hmax = hlist[0]
    for h in hlist:
        histogram = rf.Get(h)
        if histogram.GetEntries() > emax:
            emax = histogram.GetEntries()
            hmax = h
    print "Biggest histo is ", hmax
    return hmax

def FindNamedHistos(hlist,namestring,nEntries=-1):
    """This function returns a list of functions from the given list that contain the given name string"""
    rtList = []
    import re
    for h in hlist:
        r = re.compile(namestring)
        if r.search(h):
            rtList.append(h)
    return rtList

def FindNamedHistosEndingWith(hlist,namestring,nEntries=-1):
    rtList = []
    import re
    for h in hlist:
        index = len(namestring)
        if h[-index:]==namestring:
            rtList.append(h)
    return rtList
def FindNamedHistosPt(hlist,namestring,ptBinNumber,nEntries=-1):
    """This function returns a list of histograms with the correct Pt bin number and containing the specified string"""
    rtlist = []
    import re
    for h in hlist:

        if getPtBinNumber(h)!=ptBinNumber:
            continue
        r = re.compile(namestring)
        if r.search(h):
            rtlist.append(h)
    return rtlist

def GetListObjects(fileName,minEntries=-1):
    """Returns a list of names of objects in a rootfile"""
    f = ROOT.TFile(fileName)
    objects = []
    for key in f.GetListOfKeys():
        name = key.GetName()
        if minEntries > -1:
            h = f.Get(name)
            entries = h.GetEntries()
            if entries > minEntries:
                objects.append(name)
            continue
        else:
            objects.append(name)
            continue

    return objects

def PlotNamesFromPlots(directory,suffix=".pdf"):
    """this function returns a list of lists of plots names and pt bin numbers"""
    import glob
    pdfl = glob.glob(directory+"*"+suffix)
    plotNames = []
    for plot in pdfl:
        name = plot.split('/')[-1]
        name = name.strip(".pdf")
        PtBin = name.split("PtBin")[1]
        plotNames.append([name,PtBin])

    return plotNames

def PlotsByPtBin(PlotNames,PtBins):
    """returns a list of lists of the plots by Pt bin"""
    byPtBin = []
    for i in PtBins:
        byPtBin.append([])
    #have to do this like this because [[]]*10 give ten copies of the same list!
    for plot in PlotNames:
        Pt = getPtBinNumber(plot)
        bin = int(Pt)
        #print plot, bin
        byPtBin[bin].append(plot)
    #put the plot name in the appropriate list
    return byPtBin

def getBiggestPtHistos(rf,histonameString,PtBins):
    """Returns list of histograms one for each pt bin"""
    #get list of all histograms
    histos = GetListObjects(rf,35)
    #get list of those with the right names
    AsymProfs = FindNamedHistos(histos,histonameString)
    AsymProfs2 = []
    for p in AsymProfs:
        if p.find('NPV')>-1:
            continue
        AsymProfs2.append(p)
    #put these in a list by their Pt bins
    byPtBin = PlotsByPtBin(AsymProfs2,PtBins)
    #now select the bigest in each pt bins
    BestPlots = []
    for (i,pTbin) in enumerate(byPtBin):
        if len(pTbin) < 1:
            continue
        maxEntries = 0
        maxPlotName = None
        biggestH = BiggestHisto(pTbin,rf) #This function returns the histo with most entries
        BestPlots.append([biggestH,i])
    return BestPlots #this is a list of histogram names (I think!)

def draw5ppLimits():
    hline = ROOT.TLine(-4.5,1.,4.5,1.)
    hline.SetLineColor(1)
    hline.SetLineStyle(2)
    hline.Draw('Same')

    UpLine  = ROOT.TLine(-4.5,1.05,4.5,1.05)
    UpLine.SetLineColor(2)
    UpLine.SetLineStyle(2)
    UpLine.Draw('Same')

    DLine  = ROOT.TLine(-4.5,0.95,4.5,0.95)
    DLine.SetLineColor(2)
    DLine.SetLineStyle(2)
    DLine.Draw('Same')


def makeRatioGraph(list1,list2):
    """This function makes a ratio graph from two lists that are expected to be of form [ x,y,xer,yer] where these are arraygssecond list is a  lists..."""
    import ROOT
    from array import array
    if len(list1) != len(list2):
        print "Cannot make ratio plot!"
        return

    x =array("d",[])
    y = array("d",[])
    xer = array("d",[])
    yer = array("d",[])

    for (i,point) in enumerate(list1[0]):
        MCindex = None
        DataPoint = [point,list1[1][i],list1[2][i],list1[3][i]]
        for j in range(len(list1[0])):
            try:
                if list2[0][j]==point:
                    MCindex = j
            except(IndexError):
                continue
        if MCindex == None:
            continue #if there isn't an MC bin then can't make ratio
        try:
            MCpoint = [list2[0][MCindex],list2[1][MCindex],list2[2][MCindex],list2[3][MCindex]]
        except(TypeError):
            #print type(MCindex)
            #print "MCindex=",MCindex
            sys.exit()
         # print "MCpoint=",MCpoint

        if point==None or MCpoint==None:
            continue
            #some points will be none type because
            #they have no entries

        x.append(point)

        y.append(MCpoint[1]/DataPoint[1])
        xer.append(DataPoint[2])
        Yerror2 = DataPoint[3]**2 + MCpoint[3]**2
        Yerror = ROOT.TMath.Sqrt(Yerror2)
        yer.append(Yerror)
    try:
        rg = ROOT.TGraphErrors(len(x),x,y,xer,yer)
        return rg
    except(TypeError):
        print "caught exception typeerror, returning 0"
        return 0


def getPtBinNumber(name):
    """This will return the string that corresponds to the bin number taken from the name"""
    index = name.find("PtBin")
    if index == -1:
        print "No PtBin number bit"
        return None
    PtBinNumber = name[index+5:index+7]
    #print "Test ptbinnumber is ", PtBinNumber
    try:
        PtBinNumber = int(PtBinNumber)
    except(ValueError):
        PtBinNumber = int(PtBinNumber[0])
    except:
        print "achtung can't make an integer, PtBin value is ",PtBinNumber
        assert False
    return PtBinNumber

def getJSampleNumber(name):
    """This returns the J sample number"""
    index = name.find("_J")
    if index == -1:
        print "No jsample name found"
        return None
    jnumber = name[index+2]
    return jnumber
