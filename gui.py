import tkinter as tk
from tkinter import ttk

def clicked():
    l1.configure (text="Button was clicked !!")
#

# categories needs to be pulled from the database
def init_GUI(categories):
    # Initialize the title
    top.title("Budget Program")

    top.geometry('350x200')

    style.layout("TMenubutton", [
    ("Menubutton.background", None),
    ("Menubutton.button", {"children":
        [("Menubutton.focus", {"children":
            [("Menubutton.padding", {"children":
                [("Menubutton.label", {"side": "right", "expand": 1})]
            })]
        })]
    }),
    ])
    
    mbtn.menu =  tk.Menu(mbtn, tearoff = 0)
    mbtn["menu"] =  mbtn.menu
    # define Categories
    ctgory = []
    categories.sort()
    for category in categories:
        mbtn.menu.add_checkbutton(label=category, variable=ctgory.append(0))
    #
    mbtn.menu.add_separator()
    mbtn.menu.add_command(label="Clear")
    mbtn.pack()
#

def run_GUI():
    top.mainloop()
#

# Global Objects
top = tk.Tk()
l1 = tk.Label(top, text="hello", font=("Arial Bold", 50))
bt = tk.Button(top, text="Enter", bg="orange", fg="green", command=clicked)
style = ttk.Style()
mbtn = ttk.Menubutton(top, text='CategorySelect')


if __name__ == "__main__":
    init_GUI(['Groceries', 'Electronics', 'Gas', 'Dining', 'Bars', 'Entertainment', 'Subscriptions', 'Rent', 'Physical', 'Utilities', \
        'Car', 'Motorcycle', 'Insurance', 'Vacation', 'Books', 'Bicycle'])
    run_GUI()