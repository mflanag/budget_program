import tkinter as tk
from tkinter import ttk

def update_db():
    # update the database
    # update the button to show good
    bt.configure (text="Database Updated")
#

def clear_checks():
    map(lambda x: 0, ctgory)
#

# categories needs to be pulled from the database
def init_GUI(categories):
    # Initialize the title
    top.title("Budget Program")

    top.geometry('350x200')

    mbtn.menu =  tk.Menu(mbtn, tearoff = 0)
    mbtn["menu"] =  mbtn.menu
    # define Categories
    categories.sort()
    for category in categories:
        mbtn.menu.add_checkbutton(label=category, variable=ctgory.append(0))
    #
    mbtn.menu.add_separator()
    mbtn.menu.add_command(label="Clear", command=clear_checks)
    mbtn.pack()
#

def run_GUI():
    top.mainloop()
#

# Global Objects
top = tk.Tk()
cat = tk.Label(top, text="Category", font=("Arial Bold", 50))
cost = tk.Entry(top, text="Cost")
bt = tk.Button(top, text="Enter Record", bg="orange", fg="green", command=update_db)
style = ttk.Style()
mbtn = ttk.Menubutton(top, text='CategorySelect')

ctgory = []

if __name__ == "__main__":
    init_GUI(['Groceries', 'Electronics', 'Gas', 'Dining', 'Bars', 'Entertainment', 'Subscriptions', 'Rent', 'Physical', 'Utilities', \
        'Car', 'Motorcycle', 'Insurance', 'Vacation', 'Books', 'Bicycle'])
    print(style.layout('TButton'))
    print(style.element_options('TButton.label'))
    run_GUI()