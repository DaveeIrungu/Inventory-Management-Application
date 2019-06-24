# The front end
from tkinter import *
from backend import Database

database = Database("store.db")


def get_selected_row(event):
    global selected_tuple
    # Add [0] to obtain just the 1st item (the index) on the tuple
    index = list1.curselection()[0]
    # Obtain all the values on the selected row
    selected_tuple = list1.get(index)

    # Fill the entry widgets with the selected item using insert function
    # First empty of existing contents
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_onClick():
    # Before executing, first clear the listbox to eliminate redundancy
    list1.delete(0, END)
    for row in database.view():
        # The end argument ensures that every new row is put on a new line in the listbox during iteration
        list1.insert(END, row)


def search_onClick():
    # Clear the listbox before executing
    list1.delete(0, END)
    # .get() captures the input entered in the entry widgets
    for row in database.search(name_text.get(), manufacturer_text.get(), serial_text.get(), year_text.get()):
        # Insert all the values in the listbox
        list1.insert(END, row)


def insert_onCLick():
    list1.delete(0, END)
    database.insert(name_text.get(), manufacturer_text.get(), serial_text.get(), year_text.get())
    # Display these values on the listbox
    list1.insert(END, (name_text.get(), manufacturer_text.get(), serial_text.get(), year_text.get()))


def delete_onClick():
    database.delete(selected_tuple[0])


def update_onClick():
    database.update(selected_tuple[0], name_text.get(), manufacturer_text.get(), serial_text.get(), year_text.get())


window = Tk()

# Name of application on title bar
window.wm_title("Inventory Management Application")

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
# Bind method to bind a function the listbox event, ie. selected row to be deleted/updated
list1.bind('<<ListboxSelect>>', get_selected_row)
# Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=4, column=2, rowspan=6)

# Configure the listbox and scrollbar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Button objects
# Careful not to add () at the command function
b1 = Button(window, text="Add", width=12, command=insert_onCLick)
b1.grid(row=2, column=3)
b2 = Button(window, text="Delete", width=12, command=delete_onClick)
b2.grid(row=3, column=3)
b3 = Button(window, text="Update", width=12, command=update_onClick)
b3.grid(row=4, column=3)
b4 = Button(window, text="Search", width=12, command=search_onClick)
b4.grid(row=5, column=3)
b5 = Button(window, text="View All", width=12, command=view_onClick)
b5.grid(row=6, column=3)
b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
