from tkinter import *

window = Tk()

# Label objects
l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="Manufacturer")
l2.grid(row=1, column=0)

l3 = Label(window, text="Serial")
l3.grid(row=2, column=0)

l4 = Label(window, text="Year")
l4.grid(row=3, column=0)

# Entry objects
name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

manufacturer_text = StringVar()
e2 = Entry(window, textvariable=manufacturer_text)
e2.grid(row=1, column=1)

serial_text = StringVar()
e3 = Entry(window, textvariable=serial_text)
e3.grid(row=2, column=1)

year_text = StringVar()
e4 = Entry(window, textvariable=year_text)
e4.grid(row=3, column=1)

window.mainloop()
