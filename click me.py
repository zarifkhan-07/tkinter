from tkinter import *
root=Tk()
root.title("Button")
root.geometry("400x500")

def handle_pressed(event):
    print(event.char)

root.bind("<key>",handle_pressed)

def handle_click(event):
    print("\nThe button was clicked!")

button=Button(text="Click Me!!")
button.pack()

button.bind("<Button-1>", handle_click)

root.mainloop()