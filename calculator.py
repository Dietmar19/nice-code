from tkinter import*
from tkinter import font

def output():
    if check1.get() + check2.get() + check3.get() + check4.get() > 1:
        print("You choose too many values")
    else:
        number1=float(input1.get())
        number2=float(input2.get())
    if check1.get():
        output=round(number1+number2,2)
    if check2.get():
        output=round(number1-number2,2)
    if check3.get():
        output=round(number1*number2,2)
    if check4.get():
        output=round(number1/number2,2)
    else:
        print("You must choose + or - or * or /")
    output1.delete(0,END)
    output1.insert(0, output)

window=Tk()

window.geometry("570x280")

window.title("Python Calculator")
label1=Label(window, text="Calculator", fg="red", bg="black", font=("Arial, 32"))
#label.pack(expand=1)
button=Button(window, text="calculate", width=8, height=2, command=output, fg="green", bg="white", font=("Ariel", 8))
#button.pack(expand=1)
input1=Entry(fg="black", bg="yellow", font=("Arial", 12))
input2=Entry(fg="black", bg="yellow", font=("Arial", 12))
output1=Entry(fg="black", bg="green", font=("Arial", 12))

check1=IntVar()
check2=IntVar()
check3=IntVar()
check4=IntVar()

checkbutton1=Checkbutton(window, text="Plus", variable=check1)
checkbutton2=Checkbutton(window, text="MInus", variable=check2)
checkbutton3=Checkbutton(window, text="multiplicate", variable=check3)
checkbutton4=Checkbutton(window, text="divide", variable=check4)

label1.grid(row=0, column=1,padx=10, pady=10, columnspan=10)
input1.grid(row=1, column=1, padx=10, pady=10)
input2.grid(row=1, column=2, padx=10, pady=10)
checkbutton1.grid(row=2, column=0, padx=10, pady=10)
checkbutton2.grid(row=2, column=1, padx=10, pady=10)
checkbutton3.grid(row=2, column=2, padx=10, pady=10)
checkbutton4.grid(row=2, column=3, padx=10, pady=10)

button.grid(row=3, column=1, columnspan=2, pady=10)

output1.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()

