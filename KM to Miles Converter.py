from tkinter import *

tkinter = Tk()
tkinter.title("Kilometer to Miles Converter")

tkinter.minsize(600, 200)
label1 = Label(tkinter, text="Please enter how many kilometers you need to convert:")
label1.place(x=10, y=20)

entry1 = Entry(tkinter)
entry1.get()
entry1.place(x=350, y=15)

label2 = Label(tkinter, text=0, font=("Arial", 18))
label2.place(x=260, y=100)

label3 = Label(tkinter, text="Here is the answer:")
label3.place(x=230, y=80)

def convert():
    km = float(entry1.get())
    answer = round((km * 1.60934),2)
    label2.config(text=f"{answer}")


button = Button(text="Convert", command = convert)
button.place(x=240, y=150)



tkinter.mainloop()