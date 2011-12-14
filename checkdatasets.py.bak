import sys, commands, os, string, optparse

usage = "python checkdatasets [opts] \"<search string>\""
epilog = "NB: search string should be given as a string or with escaped wildcards."
parser = optparse.OptionParser(usage=usage, epilog=epilog)
parser.add_option("-d", "--download", default = False, action = "store_true",
   help = "Download any missing files.")
(opts, args) = parser.parse_args()

if len(args) != 1:
   print "Error: no/multiple search strings found."
   parser.print_help()
   sys.exit()

searchstring = args[0]

print "Checking local files..."
dudata = {}
duinfo = commands.getoutput("du -b -a %s" % searchstring.replace("/", "*"))
duinfo = duinfo.split("\n")
for line in duinfo:
   if ".root" in line:
      line = line.split()
      bytes = int(line[0])
      path = line[1]
      fn = os.path.split(path)[1]
      dudata[fn] = bytes
print "Found %d local files." % len(dudata)

print "Checking grid files..."
print searchstring
files = {}
dq2data = {}
dq2info = commands.getoutput("dq2-ls -f %s" % searchstring.replace("*", "\*"))
dq2info = dq2info.split("\n")
dataset = ""
for line in dq2info:
   if len(line) > 0 and line[-1] == "/":
      dataset = line
      print "Found dataset: %s" % dataset
   if ".root" in line:
      line = line.split()
      fn = line[2]
      bytes = int(line[-1])
      dq2data[fn] = bytes
      files[fn] = dataset
print "Found %d grid files." % len(dq2data)

print "comparing..."
wrong = 0
retry = []
for fn in dq2data:
   if fn not in dudata:
      print "%s missing (%s)." % (fn, files[fn])
      wrong += 1
      if files[fn] not in retry:
         retry.append(files[fn])
   else:
      if dq2data[fn] != dudata[fn]:
         print "%s has wrong size: local size = %d, grid size = %d." % (dudata[fn], dq2data[fn])
         wrong += 1
if wrong == 0:
   print "Local files complete."
else:
   print "%d files are missing/incomplete." % wrong
if len(retry) > 0:
   if opts.download:
      print "dq2-getting the following %d datasets:" % len(retry)
      for ds in retry:
         print "   %s" % ds
      for ds in retry:
         os.system("dq2-get %s" % ds)
   else:
      print "dq2-get the following %d datasets:" % len(retry)
      for ds in retry:
         print "   %s" % ds
