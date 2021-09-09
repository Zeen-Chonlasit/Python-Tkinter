from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/Users/chonl/Downloads/icons8-go-back-64.png')

# Showinfo, Showwarning, Showerror, Askquestion, Askokcancel, Askyesno
def popup():
    response = messagebox.showinfo("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()
    # if response == "yes":
    #     Label(root, text="You Clicked Yes!").pack()
    # else:
    #     Label(root, text="You Clicked No!").pack()

Button(root, text="Popup", command=popup).pack()

mainloop()