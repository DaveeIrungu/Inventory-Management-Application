# The front end
from tkinter import *
from backend import Database

database = Database("store.db")


class Window:

    def __init__(self, window):
        self.window = window
        self.window.wm_title("Inventory Management Application")

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
        self.name_text = StringVar()
        self.e1 = Entry(window, textvariable=self.name_text)
        self.e1.grid(row=0, column=1)

        self.manufacturer_text = StringVar()
        self.e2 = Entry(window, textvariable=self.manufacturer_text)
        self.e2.grid(row=0, column=3)

        self.serial_text = StringVar()
        self.e3 = Entry(window, textvariable=self.serial_text)
        self.e3.grid(row=1, column=1)

        self.year_text = StringVar()
        self.e4 = Entry(window, textvariable=self.year_text)
        self.e4.grid(row=1, column=3)

        # Listbox object
        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)
        # Bind method to bind a function the listbox event, ie. selected row to be deleted/updated
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # Scrollbar
        sb1 = Scrollbar(window)
        sb1.grid(row=4, column=2, rowspan=6)

        # Configure the listbox and scrollbar
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        # Button objects
        # Careful not to add () at the command function
        b1 = Button(window, text="Add", width=12, command=self.insert_onCLick)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Delete", width=12, command=self.delete_onClick)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Update", width=12, command=self.update_onClick)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Search", width=12, command=self.search_onClick)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="View All", width=12, command=self.view_onClick)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    def get_selected_row(self, event):
        global selected_tuple
        # Add [0] to obtain just the 1st item (the index) on the tuple
        index = self.list1.curselection()[0]
        # Obtain all the values on the selected row
        selected_tuple = self.list1.get(index)

        # Fill the entry widgets with the selected item using insert function
        # First empty of existing contents
        self.e1.delete(0, END)
        self.e1.insert(END, selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, selected_tuple[2])
        self.e3.delete(0, END)
        self.e3.insert(END, selected_tuple[3])
        self.e4.delete(0, END)
        self.e4.insert(END, selected_tuple[4])

    def view_onClick(self):
        # Before executing, first clear the listbox to eliminate redundancy
        self.list1.delete(0, END)
        for row in database.view():
            # The end argument ensures that every new row is put on a new line in the listbox during iteration
            self.list1.insert(END, row)

    def search_onClick(self):
        # Clear the listbox before executing
        self.list1.delete(0, END)
        # .get() captures the input entered in the entry widgets
        for row in database.search(self.name_text.get(), self.manufacturer_text.get(), self.serial_text.get(),
                                   self.year_text.get()):
            # Insert all the values in the listbox
            self.list1.insert(END, row)

    def insert_onCLick(self):
        self.list1.delete(0, END)
        database.insert(self.name_text.get(), self.manufacturer_text.get(), self.serial_text.get(),
                        self.year_text.get())
        # Display these values on the listbox
        self.list1.insert(END, (
            self.name_text.get(), self.manufacturer_text.get(), self.serial_text.get(), self.year_text.get()))

    def delete_onClick(self):
        database.delete(selected_tuple[0])

    def update_onClick(self):
        database.update(selected_tuple[0], self.name_text.get(), self.manufacturer_text.get(), self.serial_text.get(),
                        self.year_text.get())


window = Tk()
Window(window)
window.mainloop()
