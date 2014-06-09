#!/usr/bin/python


# imports
import sys
import operator
import time

def checkPython():
	'''(none) -> int'''
	# checks Python version
	version = int((sys.version)[0])
	return version

# import tkinter for Python 2 and 3
if checkPython() == 2:
	from Tkinter import *
	import tkFileDialog as filedialog
elif  checkPython() == 3:
	from tkinter import *
else:
	sys.exit('Python version error!!\nPlease install Python 2.7.x or Python 3.x')



# main class
class TextFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)   

		self.parent = parent        
		self.initUI()

	def initUI(self):

		self.parent.title("File dialog")
		self.pack(fill=BOTH, expand=1)
		
		# menu
		menubar = Menu(self.parent)
		self.parent.config(menu=menubar)

		fileMenu = Menu(menubar)
		fileMenu.add_command(label="Analyze FASTA file", command=self.openFile)
		fileMenu.add_command(label="Analyze FAS folder", command=self.getFolder)
		fileMenu.add_command(label="Save results", command=self.openFile)
		fileMenu.add_command(label="Preferences...", command=self.openFile)
		fileMenu.add_command(label="Quit aMof", command=self.exit_)
		menubar.add_cascade(label="File", menu=fileMenu)        

		self.txt = Text(self)
		self.txt.pack(fill=BOTH, expand=1)

		# buttons
		b1 = Button(root, text="Open FASTA", command=self.openFile)
		b1.pack(side=LEFT)
		b2 = Button(root, text="Make fasta from folder", command=self.getFolder)
		b2.pack(side=LEFT)
		b2 = Button(root, text="MoF it!", command=self.getFolder)
		b2.pack(side=LEFT)

	# methods
	def readFile(self, filename):
		f = open(filename, "r")
		text = f.read()
		return text


	def openFile(self):
		ftypes = [('Text files', '*.txt'), ('All files', '*')]
		dlg = filedialog.Open(self, filetypes = ftypes)
		filename = dlg.show()
		if filename != '':
			text = self.readFile(filename)
			self.txt.insert(END, text)


	def analyzeFASTA(self):
		filename = filedialog.askopenfilename([('Text files', '*.txt'), ('All files', '*')])
		print(filename)       

    def getFileName(self):
    	filename = filedialog.askopenfilename([('Text files', '*.txt'), ('All files', '*')])
        return filename
        
	def getFolderName(self):
		foldername = filedialog.askdirectory(parent=root,initialdir="/", title='Select the folder containing the FAS files')
		return foldername

	def exit_(self):
		global root
		root.quit()
		root.destroy()



# body
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
	
	#global top

    

    

if __name__ == '__main__':
    main()
