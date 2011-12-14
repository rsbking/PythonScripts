##Python script to take input list of png's or use all png's
##in the current working directory
import glob

pngs =  glob.glob("*.pngs")



def wrapHeaders(text):
    """Function that takes one argument, and wraps it with
    headers and footers so that it becomes a proper latex document"""



def wrapImage(image,caption=None):
    """Function which wraps an image file path with latex crap"""

    outText = "\\begin{figure} \n"
    outText += "\\begin{center} \n"
    outText += "\\reflectbox{\\includegraphics{"+image+"}} \n"
    outText += "\\end{center} \n"
    if caption:
        outText += "\\caption{"+caption+"} \n"
    #outText += "\\label{toucan} \n"
    outText += "\\end{figure} \n"

    return outText

def LayoutImages(images):
    """Function takes a list of latex includegraphics bits and
    makes a nice latex layout of them"""
