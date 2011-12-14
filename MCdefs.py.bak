#define class for MC samples I use with useful info:
import ROOT,MCmetaReader
class MCsample:
	
	def __init__(self,RunNumb,name,filename,color,XS=0,kFactor=1,efficency=1):
		"""intializer. The arguments are 
		RunNumber: to get the correct meta data from the meta data reader,
		name: a readable name which is the filename without the '.root'
		color: a color variable for root. Within this file there is a dictionary defining these colors"""
		self.RunNumber = RunNumb
		self.name = name #something nice and human
		self.filename = filename #the longer name
		try:
			self.efficency = MCmetaReader.getFilterEff(RunNumb)
			self.kFactor = MCmetaReader.getMCkfactor(RunNumb)
			self.XS = MCmetaReader.getMCXS(RunNumb)
			self.XSeff = self.XS * self.kFactor * self.efficency
		except(AssertionError):
			self.efficency = MCmetaReader.getFilterEff(RunNumb)
			self.kFactor = MCmetaReader.getMCkfactor(RunNumb)
			self.XS = MCmetaReader.getMCXS(RunNumb)
			self.XSeff = self.XS * self.kFactor * self.efficency
		self.color = color
		self.Nentries = 0 #this is intialized to Zero. Can be filled at use if desired
		self.weight = 0
		
##now define objects for all the MC files I need:

#dictionary for the colors for various samples
colors = {'signal':ROOT.kWhite,'WNp0':ROOT.kOrange+4,'WNp1':ROOT.kOrange+3,'WNp2':ROOT.kRed,'WNp3':ROOT.kRed+2,'WNp4':ROOT.kBlue-6,'WNp5':ROOT.kBlue-10,
'Wmunu':ROOT.kTeal,
'Wtaunu':ROOT.kOrange,
'Z':ROOT.kBlue,
'top':ROOT.kGreen,
'single top':ROOT.kGreen+3,
'WHeavyFlavour':ROOT.kPink+8,
"Sherpa":ROOT.kGreen-10
}


#WW

WW = MCsample(105985,"WW","WW_Herwig.root",colors["signal"])
WZ = MCsample(105987,"WZ","WZ_Herwig.root",colors["signal"])

#Wenu:
WenuNp0 = MCsample(107680,"WenuNp0","AlpgenJimmyWenuNp0_pt20.root",colors["WNp0"])
WenuNp1 = MCsample(107681,"WenuNp1","AlpgenJimmyWenuNp1_pt20.root",colors["WNp1"])
WenuNp2 = MCsample(107682,"WenuNp2","AlpgenJimmyWenuNp2_pt20.root",colors["WNp2"])
WenuNp3 = MCsample(107683,"WenuNp3","AlpgenJimmyWenuNp3_pt20.root",colors["WNp3"])
WenuNp4 = MCsample(107684,"WenuNp4","AlpgenJimmyWenuNp4_pt20.root",colors["WNp4"])
WenuNp5 = MCsample(107685,"WenuNp5","AlpgenJimmyWenuNp5_pt20.root",colors["WNp5"])

Wenu = [WenuNp0,WenuNp1,WenuNp2,WenuNp3,WenuNp4,WenuNp5]

#Wmunu
WmunuNp0 = MCsample(107690,"WmunuNp0","AlpgenJimmyWmunuNp0_pt20.root",colors["WNp0"])
WmunuNp1 = MCsample(107691,"WmunuNp1","AlpgenJimmyWmunuNp1_pt20.root",colors["WNp1"])
WmunuNp2 = MCsample(107692,"WmunuNp2","AlpgenJimmyWmunuNp2_pt20.root",colors["WNp2"])
WmunuNp3 = MCsample(107693,"WmunuNp3","AlpgenJimmyWmunuNp3_pt20.root",colors["WNp3"])
WmunuNp4 = MCsample(107694,"WmunuNp4","AlpgenJimmyWmunuNp4_pt20.root",colors["WNp4"])
WmunuNp5 = MCsample(107695,"WmunuNp5","AlpgenJimmyWmunuNp5_pt20.root",colors["WNp5"])

Wmunu = [WmunuNp0,WmunuNp1,WmunuNp2,WmunuNp3,WmunuNp4,WmunuNp5]

#Wtaunu
WtaunuNp0 = MCsample(107700,"WtaunuNp0","AlpgenJimmyWtaunuNp0_pt20.root",colors["Wtaunu"])
WtaunuNp1 = MCsample(107701,"WtaunuNp1","AlpgenJimmyWtaunuNp1_pt20.root",colors["Wtaunu"])
WtaunuNp2 = MCsample(107702,"WtaunuNp2","AlpgenJimmyWtaunuNp2_pt20.root",colors["Wtaunu"])
WtaunuNp3 = MCsample(107703,"WtaunuNp3","AlpgenJimmyWtaunuNp3_pt20.root",colors["Wtaunu"])
WtaunuNp4 = MCsample(107704,"WtaunuNp4","AlpgenJimmyWtaunuNp4_pt20.root",colors["Wtaunu"])
WtaunuNp5 = MCsample(107705,"WtaunuNp5","AlpgenJimmyWtaunuNp5_pt20.root",colors["Wtaunu"])

Wtaunu = [WtaunuNp0,WtaunuNp1,WtaunuNp2,WtaunuNp3,WtaunuNp4,WtaunuNp5]

#Wheavy flavour
WbbNp0 = MCsample(107280,"WbbFullNp0","AlpgenJimmyWbbFullNp0_pt20.root",colors["WHeavyFlavour"])
WbbNp1 = MCsample(107281,"WbbFullNp1","AlpgenJimmyWbbFullNp1_pt20.root",colors["WHeavyFlavour"])
WbbNp2 = MCsample(107282,"WbbFullNp2","AlpgenJimmyWbbFullNp2_pt20.root",colors["WHeavyFlavour"])
WbbNp3 = MCsample(107283,"WbbFullNp3","AlpgenJimmyWbbFullNp3_pt20.root",colors["WHeavyFlavour"])

WccNp0 = MCsample(117284,"WccFullNp0","AlpgenWccFullNp0_pt20.root",colors["WHeavyFlavour"])
WccNp1 = MCsample(117285,"WccFullNp1","AlpgenWccFullNp1_pt20.root",colors["WHeavyFlavour"])
WccNp2 = MCsample(117286,"WccFullNp2","AlpgenWccFullNp2_pt20.root",colors["WHeavyFlavour"])
WccNp3 = MCsample(117287,"WccFullNp3","AlpgenWccFullNp3_pt20.root",colors["WHeavyFlavour"])

WcNp0 = MCsample(117293,"WcNp0","AlpgenWcNp0_pt20.root",colors["WHeavyFlavour"])
WcNp1 = MCsample(117294,"WcNp1","AlpgenWcNp1_pt20.root",colors["WHeavyFlavour"])
WcNp2 = MCsample(117295,"WcNp2","AlpgenWcNp2_pt20.root",colors["WHeavyFlavour"])
WcNp3 = MCsample(117296,"WcNp3","AlpgenWcNp3_pt20.root",colors["WHeavyFlavour"])
WcNp4 = MCsample(117297,"WcNp4","AlpgenWcNp4_pt20.root",colors["WHeavyFlavour"])

Whf = [WbbNp0,WbbNp1, WbbNp2,WbbNp3,WccNp0,WccNp1,WccNp2,WccNp3,WcNp0,WcNp1,WcNp2,WcNp3,WcNp4]

#Z
ZeeNp0 = MCsample(107650,"ZeeNp0","AlpgenJimmyZeeNp0_pt20.root",colors["Z"])
ZeeNp1 = MCsample(107651,"ZeeNp1","AlpgenJimmyZeeNp1_pt20.root",colors["Z"])
ZeeNp2 = MCsample(107652,"ZeeNp2","AlpgenJimmyZeeNp2_pt20.root",colors["Z"])
ZeeNp3 = MCsample(107653,"ZeeNp3","AlpgenJimmyZeeNp3_pt20.root",colors["Z"])
ZeeNp4 = MCsample(107654,"ZeeNp4","AlpgenJimmyZeeNp4_pt20.root",colors["Z"])
ZeeNp5 = MCsample(107655,"ZeeNp5","AlpgenJimmyZeeNp5_pt20.root",colors["Z"])

ZmumuNp0 = MCsample(107660,"ZmumuNp0","AlpgenJimmyZmumuNp0_pt20.root",colors["Z"])
ZmumuNp1 = MCsample(107661,"ZmumuNp1","AlpgenJimmyZmumuNp1_pt20.root",colors["Z"])
ZmumuNp2 = MCsample(107662,"ZmumuNp2","AlpgenJimmyZmumuNp2_pt20.root",colors["Z"])
ZmumuNp3 = MCsample(107663,"ZmumuNp3","AlpgenJimmyZmumuNp3_pt20.root",colors["Z"])
ZmumuNp4 = MCsample(107664,"ZmumuNp4","AlpgenJimmyZmumuNp4_pt20.root",colors["Z"])
ZmumuNp5 = MCsample(107665,"ZmumuNp5","AlpgenJimmyZmumuNp5_pt20.root",colors["Z"])

ZtautauNp0 = MCsample(107670,"ZtautauNp0","AlpgenJimmyZtautauNp0_pt20.root",colors["Z"])
ZtautauNp1 = MCsample(107671,"ZtautauNp1","AlpgenJimmyZtautauNp1_pt20.root",colors["Z"])
ZtautauNp2 = MCsample(107672,"ZtautauNp2","AlpgenJimmyZtautauNp2_pt20.root",colors["Z"])
ZtautauNp3 = MCsample(107673,"ZtautauNp3","AlpgenJimmyZtautauNp3_pt20.root",colors["Z"])
ZtautauNp4 = MCsample(107674,"ZtautauNp4","AlpgenJimmyZtautauNp4_pt20.root",colors["Z"])
ZtautauNp5 = MCsample(107675,"ZtautauNp5","AlpgenJimmyZtautauNp5_pt20.root",colors["Z"])


Z = [ZeeNp0,ZeeNp1,ZeeNp2,ZeeNp3,ZeeNp4,ZeeNp5,ZmumuNp0,ZmumuNp1,ZmumuNp2,ZmumuNp3,ZmumuNp4,ZmumuNp5,ZtautauNp0,ZtautauNp1,ZtautauNp2,ZtautauNp3,ZtautauNp4,ZtautauNp5]

#top
top = MCsample(105200,"Top","T1_McAtNlo_Jimmy.root",colors["top"])

#single top
st_tchan_enu = MCsample(108340,"st_tchan_enu","st_tchan_enu_McAtNlo_Jimmy.root",colors["single top"])
st_tchan_munu = MCsample(108341,"st_tchan_munu","st_tchan_munu_McAtNlo_Jimmy.root",colors["single top"])
st_tchan_taunu = MCsample(108342,"st_tchan_taunu","st_tchan_taunu_McAtNlo_Jimmy.root",colors["single top"])
st_schan_enu = MCsample(108343,"st_schan_enu","st_schan_enu_McAtNlo_Jimmy.root",colors["single top"])
st_schan_munu = MCsample(108344,"st_schan_munu","st_schan_munu_McAtNlo_Jimmy.root",colors["single top"])
st_schan_taunu = MCsample(108345,"st_schan_taunu","st_schan_taunu_McAtNlo_Jimmy.root",colors["single top"])

singleTop = [st_tchan_enu,st_tchan_munu,st_tchan_taunu,st_schan_enu,st_schan_munu,st_schan_taunu]

#define the jet samples here too:
SherpaWenuJets = MCsample(119128,"SherpaWenuJets","SherpaW5jetstoenu30GeVScaleMT.root",colors["Sherpa"])