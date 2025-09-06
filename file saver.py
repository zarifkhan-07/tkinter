from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

root=Tk()
root.geometry("400x300")
root.title("File save")
root.rowconfigure(0,minsize=800,weight=1)
root.columnconfigure(1,minsize=800,weight=1)

def open_file():
    file_path=askopenfilename(
        file_type=[("Text Files","*.txt"),("All Files","*.*")])
    if not file_path:
        return
    txt_edit.delete(1.0,END)

    with open(file_path,"r") as input_file:
        text=input_file.read
        txt_edit.insert(END,text)
        input_file.close()
    root.title(f"Codingal's text editor - {file_path}")

def save_file():
    file_path=asksaveasfilename(
        defaultextension="txt",
        file_type=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if not file_path:
        return
    with open(file_path,"w") as output_file:
        txt_edit = txt_edit.get(END,text)
        output_file.write(text)
        root.title(f"Codingal's text editor - {file_path}")

text_edit=Text(root)
fr_buttons= Frame(root, relief=RAISED, bd=1)
btn_open=Button(fr_buttons, text="OPEN", command=open_file)
btn_save=Button(fr_buttons, text="SAVE", command=save_file)

btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)

fr_buttons.grid(row=0,column=0,sticky="ns")
text_edit.grid(row=0,column=1,sticky="nsew")

root.mainloop()