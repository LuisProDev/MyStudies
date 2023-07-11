from tkinter import *


def convert(event=None):
    miles = int(mile_entry.get())
    miles = round(miles * 1.602, 1)
    kilometer.delete(0, END)
    kilometer.insert(0, miles)


my_window = Tk()
my_window.title("Convert miles to kilometers")
my_window.eval('tk::PlaceWindow . center')
my_window.geometry("300x200")
my_window.config(padx=50, pady=60)
my_window.resizable(False, False)

mile_entry = Entry(width=10)
mile_entry.grid(row=0, column=1)
mile_entry.focus_set()
mile_entry.bind('<Return>', convert)

miles_label = Label(text="miles", font=("Arial", 10, "normal"))
miles_label.grid(row=0, column=2)

aux_label = Label(text="is equal to", font=("Arial", 10, "normal"))
aux_label.grid(row=1, column=0)

kilometer_label = Label(text="kilometers", font=("Arial", 10, "normal"))
kilometer_label.grid(row=1, column=2)

kilometer = Entry(width=10)
kilometer.grid(row=1, column=1)
kilometer.insert(0, "0")

convert_button = Button(text="Convert", command=convert)
convert_button.grid(row=2, column=1)


my_window.mainloop()
