from tkinter import *
#from tkinter import Frame, Tk, BOTH, Text, Menu, END, filedialog
import sys


class TextFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Analyze FASTA file", command=self.openFile)
        fileMenu.add_command(label="Analyze FAS folder", command=self.openFolder)
        fileMenu.add_command(label="Save results", command=self.openFile)
        fileMenu.add_command(label="Preferences...", command=self.openFile)
        fileMenu.add_command(label="Quit aMof", command=self.exit_)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    def openFile(self):
        ftypes = [('Text files', '*.txt'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def openFolder(self):
        dirname = filedialog.askdirectory(parent=root,initialdir="/",
                                          title='Sselect the folder containing the FAS files'

    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text

    def exit_(self):
        global root
        root.quit()
        root.destroy()


  




def main():
    global root
    root = Tk()
    main_frame = TextFrame(root)
    root.title("aMof ..by alec_djinn  --  running on " + sys.platform)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root_size = ("%dx%d" % (w/2, h/2))
    x = w/4
    y = h/4
    root_pos = ("%d+%d" % (x, y))
    root.geometry(root_size + "+" + root_pos)
    root.mainloop()

    

    

if __name__ == '__main__':
    main()
    
