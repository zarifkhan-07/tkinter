from tkinter import *
root=Tk()
root.geometry("300x400")
root.title("Parent Window")

def Topwin():
    top=Toplevel()
    top.geometry("100x200")
    top.title("Topwin")

    l = Label(top, text=("I am top left"))
    l.pack()

    top.mainloop()

l2=Label(root, text="I am the main")
l2.pack()

btn=Button(root, text="Click me to get another window", command=Topwin)
btn.pack()

root.mainloop()