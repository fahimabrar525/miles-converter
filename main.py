from tkinter import *

def miles_to_km():
    miles = float(miles_entry.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)















window.mainloop()