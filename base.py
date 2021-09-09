from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/Users/chonl/Downloads/icons8-go-back-64.png')

def open():
    global my_img
    top = Toplevel()
    top.title('My Second Window')
    top.iconbitmap('c:/Users/chonl/Downloads/icons8-go-back-64.png')
    my_img = ImageTk.PhotoImage(Image.open("images/heart.png"))
    my_label = Label(top, image=my_img).pack()  
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()



root.mainloop()