"""A group of functions for making tex output from python data containers. Scope for more functions and stuff"""

def makeTexRow(inList):
    """This function takes a list and returns a list edited so that it canform a tex table with the contents"""
    outList = []
    for (i,item) in enumerate(inList):
        outList.append(str(item) + ' & ')
    
    outList[-1] += ' \\\\ \n' #create end of row syntax
    #NB \\\\ because first slash is python string esc.!

    return outList #return the string of the row


def finalizeTable(rowList,title="default title"):
    """This function takes a list of tex table rows and completes them with header and footer returning a string so that it can just be pasted into a tex file"""
    
    ncolumns = len(rowList[0])
    columnStr = "c "
    ot = "%This is a automatically generated table from python \n"
    ot +="\\begin{table}[bt] \n"
    ot += "\\caption{"+title+"} \n"
    ot += "\\centering \n"
    ot +="\\begin{tabular}{"+ncolumns*columnStr+"} \n"
    #now add rows from list in rowList
    for row in rowList:
        for item in row:
            ot += item


    ot += "\\end{tabular} \n"
    ot += "\\end{table} \n"

    return ot
