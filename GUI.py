"""
Author: Dietmar
Datum: 11.12.2021
"""


from tkinter import*   # import alle Funktionen des Moduls
window = Tk()            # erstellt ein Fenster

window.geometry('500x200') # setzt 200Pixel hoch, 00 Pixel breit


window.title("GUI erster Versuch")
label = Label(window,text="Python Tkinter")
##label.pack(expand=5)  # aktivierung des Labels

frame=Frame(window,relief="ridge",borderwidth="20")

frame.pack(fill="both", expand=1)


window.mainloop()      # öffnet das Objekt Fenster