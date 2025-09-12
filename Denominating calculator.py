from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root=Tk()
root.configure(bg="Light blue")
root.geometry("300x400")
root.title("Denominating Calculator")

upload=Image.open("image.jpeg")

upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)

label= Label(root, image=image, bg="Light blue")
label.place(x=180, y=20)

label1= Label(root, text="Hey User!. Welcome to Dinomination Counter Application", bg="Light blue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MSGbox=messagebox.showinfo("Alert", "Do you want to calculate the domination counter.")

    if MSGbox=="ok":
        topwin()

btn1=Button(root, text="Lets get started", bg='brown', fg='white', relief=GROOVE)
btn1.place(x=260, y=360)
