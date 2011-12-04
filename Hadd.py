"""Adds a whole load of root files together... From Adrian Lewis."""
import ROOT,sys

outfile_name = sys.argv[1]
file_names = sys.argv[2:]

def get_all(f):
    """Simple convenience function that takes a TFile and
    returns a dictionary with pointers to all the objects it contains
    """

    rt_dic = {}
    for iter in f.GetListOfKeys():
        name = iter.GetName()
        print name
        print f.Get(name)
        rt_dic[name] = f.Get(name)
    return rt_dic


#then here is the bit of code that does the hadding:

f_out = ROOT.TFile(outfile_name, "RECREATE")
print "Destination File:", outfile_name
out_dict = {}
#f_ins = []
for i, fn in enumerate(file_names):
    f_in = ROOT.TFile(fn, "READ")
    #f_ins.append(f_in)
    print "Source File {0}:".format(i), fn
    hist_dict = get_all(f_in)
    for k,v in hist_dict.iteritems(): #k is the key and v is the destination
        if k in out_dict:
            out_dict[k].Add(v)
        else:
            out_dict[k] = v.Clone()
            out_dict[k].SetDirectory(f_out)
        f_in.Close()
f_out.Write()
f_out.Close()
#for f_in in f_ins:
    #f_in.Close()
