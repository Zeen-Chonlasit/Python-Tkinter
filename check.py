from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/Users/chonl/Downloads/icons8-go-back-64.png')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="Pizza", offvalue="Hamburger")
c.deselect()
c.pack()


myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()