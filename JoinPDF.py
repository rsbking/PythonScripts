#function to join multiple pdfs together into one big pdf

def join(pdfList,outname = "output.pdf"):
    """This function takes two arguments. The first is an iterable of pdf files, the second is the output pdf name, which defaults to 'output.pdf'"""
    import os
    inputString = ''
    for pdf in pdfList:
        inputString += pdf+' '
    #uses the ghostscript
    cmd = "gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile="+outname+" "+inputString+"\n"
    os.system(cmd)


if __name__=="__main__":
    import sys
    try:
        outname = sys.argv[1]
    except(IndexError):
        print "You must specify the output pdf name as the first argument. Please try again"
        sys.exit()
    inList = []
    if len(sys.argv)>2:
        inList = sys.argv[2:]
    else:
        import glob
        inList = glob.glob("*.pdf")

    join(inList,outname)

