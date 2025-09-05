import tkinter as tk

def convert():
    try:
        inches=float(entry.get())
        cm=inches*2.54
        label.config(text="Length in cm:" + str(cm))
    except ValueError:
        label.config(text="Please enter a valid number.")
root=tk.Tk()
root.title("Length Converter")
root.geometry("300x400")

label=tk.Label(root, text="Enter length as inches")
label.pack(pady=5)

entry=tk.Entry(root)
entry.pack(pady=5)

button=tk.Button(root, text="Convert", command=convert)
button.pack(pady=5)

label=tk.Label(root, text="Length in cm:")
label.pack(pady=5)

root.mainloop()