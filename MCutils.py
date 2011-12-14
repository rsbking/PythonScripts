#a Standard set of utilities that can be used for plotting MC/Data things
import ROOT
import MCdefs,RatioPlot
import random
class MCutils:
    def __init__(self,filePrefix,lumi=1):
        self.filePrefix = filePrefix #that's where the datafiles are stored
        if self.filePrefix[-1] != '/': self.filePrefix += '/'
        self.lumi = lumi
        self.openedFiles = {} # a dictionary pointing to the opened files


    def _getFile(self,fileName):
        """returns the open file"""
        try:
            rf = self.openedFiles[fileName]
        except(KeyError):
            #this means the root file hasn't been opened yet
            f = self.filePrefix+fileName
            rf = ROOT.TFile(f,"READ")
            self.openedFiles[f] = rf
        return rf


    def getScaledPlot(self, mcSampleObj,plotname):
        """mcSampleObj: an object of type MCsample
        filePrefix: the prefix required to find the root file
        plotname: the plot you want"""
        rf = self._getFile(mcSampleObj.filename)
        #print "in 'getScaledPlot' rf is: ",rf
        if not mcSampleObj.weight:
            if not mcSampleObj.Nentries:
                cutflowHist = rf.Get("Cutflow")
                if 'herpa' in mcSampleObj.name:
                    Nentries = cutflowHist.GetBinContent(4)
                Nentries = cutflowHist.GetBinContent(2)
                mcSampleObj.Nentries = Nentries

            weight = self.lumi * mcSampleObj.XSeff / mcSampleObj.Nentries
            mcSampleObj.weight = weight

        returnPlot = rf.Get(plotname)
        returnPlot.SetName(str(random.random()))
        returnPlot.Scale(mcSampleObj.weight)
        returnPlot.SetFillColor(mcSampleObj.color)
        #returnPlot.SetLineColor(mcSampleObj.color)
        return returnPlot


    def combinePlots(self,mcSampleObjList,plotname):
        """Takes a list of mcSampleObjs and a plotname. Return a combined plot which is the sum of these"""
        hlist = []
        for samp in mcSampleObjList:
            hist = self.getScaledPlot(samp,plotname)
            hlist.append(hist)
        #print "incombineplots, hlist[0] is ",hlist[0]
        baseHist = hlist[0].Clone(str(random.random()))
        #print "in Combineplots, baseHist is: ",baseHist
        for h in hlist[1:]:
            baseHist.Add(h)
        #print "and again, basehist is ",baseHist
        #ROOT.SetOwnership(baseHist,0)
        return baseHist

    def getCutFlow(self,mcSample,nCuts):
        """Returns a dictionary  of the cutflow
        if a dictionary is supplied as the second argument then will only return """
        f = self._getFile(mcSample.filename)
        cutflowHist = f.Get("Cutflow")
        outputDic = {}
        for cut in range(nCuts):
            #binKey = cutflowHist.GetBinLowEdge(binN)
            binN = cutflowHist.FindBin(cut)
            outputDic[cut] = cutflowHist.GetBinContent(binN)
        return outputDic
