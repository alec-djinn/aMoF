from  tkinter import *
root = Tk()
root.filename =  filedialog.askopenfilename(
    initialdir = "E:/Images",title = "choose your file",
    filetypes = (("text files","*.txt"),("all files","*.*")))
print(root.filename)
