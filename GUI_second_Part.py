from tkinter import*
from types import BuiltinFunctionType


window=Tk()

window.geometry("800x800")
window.title("My first Python GUI")

label=Label(window, text="first label", borderwidth=10, justify="left")
label.pack(expand=1)
frame=Frame(window,borderwidth=20, relief=(RIDGE))
frame.pack(fill=BOTH, expand=1)
def exit1():
    print("Programm beenden")
    window.destroy()
button=Button(window, text="Exit", width=20, height=10, command=exit1)
button.pack(side="left")
dict=()
def readin():
    enter=Entry()
    enter.pack()
    
    enter.insert(0, "Default")
    #enter.delete(0, "end") 
    
        
button1=Button(window,text="Read in", width=20, height=10,command=readin)
button1.pack(side="right")

scrollbar= Scrollbar(window)
listbox=Listbox(window, yscrollcommand=scrollbar.set)
list=range(50)
for item in list:
    listbox.insert(END, item)
scrollbar.config(command=listbox.yview)
listbox.pack(side="left")
scrollbar.pack(side="left", fill=BOTH)


window.mainloop()