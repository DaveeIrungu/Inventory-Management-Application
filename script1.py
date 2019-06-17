from tkinter import *

window = Tk()

# Label objects
l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="Manufacturer")
l2.grid(row=0, column=2)

l3 = Label(window, text="Serial")
l3.grid(row=1, column=0)

l4 = Label(window, text="Year")
l4.grid(row=1, column=2)

# Entry objects
name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

manufacturer_text = StringVar()
e2 = Entry(window, textvariable=manufacturer_text)
e2.grid(row=0, column=3)

serial_text = StringVar()
e3 = Entry(window, textvariable=serial_text)
e3.grid(row=1, column=1)

year_text = StringVar()
e4 = Entry(window, textvariable=year_text)
e4.grid(row=1, column=3)

# Listbox object
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=4, column=2, rowspan=6)

# Configure listbox and scrollbar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Button objects
b1 = Button(window, text="Add", width=12)
b1.grid(row=2,column=3)

b2 = Button(window, text="Delete", width=12)
b2.grid(row=3,column=3)

b3 = Button(window, text="Update", width=12)
b3.grid(row=4,column=3)

b4 = Button(window, text="Search", width=12)
b4.grid(row=5,column=3)

b5 = Button(window, text="View All", width=12)
b5.grid(row=6,column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7,column=3)

window.mainloop()
