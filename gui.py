import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
# Global Objects
top = tk.Tk()
cost = None
update_btn = None
style = ttk.Style()
category_buttons = []
ctgory = tk.StringVar()
mult_entry_state = tk.BooleanVar()

def update_db(temp=None):
    global ctgory, cost, category_buttons
    global desc, mult_entry_state
    # check that there is valid info selected
    price = cost.get()
    category_select = ctgory.get()
    description = desc.get('1.0', 'end-1c')
    if price == '':
        messagebox.showerror('Invalid Entry', 'No cost entered.')
        return
    #
    price = float(price)
    if category_select == '' and price <= 0.0:
        messagebox.showerror('Invalid Entry', \
            'Price must be greater than zero.\nYou must select a category.')
        return
    elif price <= 0.0:
        messagebox.showerror('Invalid Entry', \
            'Price must be greater than zero.')
        return
    elif category_select == '':
        messagebox.showerror('Invalid Entry', \
            'You must select a category')
        return
    #
    # update the database
    print("Categories updated %s with price %f" % (category_select, price))
    print("Memo - %s" % description)
    # update the button to show good
    multi_state = mult_entry_state.get()
    if not multi_state: # negative polarity
        messagebox.showinfo('Entry Successfully Added', \
            'Entry of (%s, %f)\nMemo - %s' % (category_select, price, description))
    #
    # clear variables
    ctgory.set('')
    cost.delete(0, 'end')
    desc.delete('1.0', 'end')
    map(lambda x: x.deselect(), category_buttons)
#

# categories needs to be pulled from the database
def init_GUI(categories):
    global ctgory, category_buttons, cost
    global mult_entry_lbl, mult_entry_chkbx
    # Initialize the title
    top.title("Budget Program")

    # define Categories
    categories.sort()
    row = 1
    col = 0
    for category in categories:
        cat_opt = tk.Radiobutton(top, text=category, \
            variable=ctgory, value=category, indicatoron=0,\
            width=20, font=('Arial Bold', 10))
        cat_opt.grid(column=col, row=row)
        cat_opt.deselect()
        category_buttons.append(cat_opt)
        col += 1
        if col % 3 == 0:
            col = 0
            row += 1
        #
    #

    # set key bindings
    cost.bind('<Return>', update_db)
    
    # set locations
    end_col = int(len(categories) / 3)
    cat_lbl.grid(column=0, row=0, columnspan=(end_col+1))
    cost.grid(column=(end_col + 1), row=1)
    cost_lbl.grid(column=(end_col+1), row=0)
    desc_lbl.grid(column=(end_col + 1), row=2)
    desc.grid(column=(end_col + 1), row=3, rowspan=5)
    mult_entry_lbl.grid(column=(end_col + 2), row = 0)
    mult_entry_chkbx.grid(column=(end_col + 3), row = 0)
    update_btn.grid(column=(end_col + 2), row=1)
#

def run_GUI():
    top.mainloop()
#

cat_lbl = tk.Label(top, text="Select a Category Below", font=("Arial Bold", 24))
cost_lbl = tk.Label(top, text="Enter Cost Below", font=("Arial", 10))
desc_lbl = tk.Label(top, text="Enter Description", font=("Arial", 10))
mult_entry_lbl = tk.Label(top, text="Add Another Entry?", font=("Arial", 10))
desc = scrolledtext.ScrolledText(top, height=5, width = 30, wrap='word')
cost = tk.Entry(top, text="Cost")
update_btn = tk.Button(top, text="Enter Record", bg="white", fg="black", command=update_db)
mult_entry_chkbx = tk.Checkbutton(top, var=mult_entry_state)

if __name__ == "__main__":
    init_GUI(['Groceries', 'Electronics', 'Gas', 'Dining', 'Bars', 'Entertainment', 'Subscriptions', 'Rent', 'Physical', 'Utilities', \
        'Car', 'Motorcycle', 'Insurance', 'Vacation', 'Books', 'Bicycle'])
    run_GUI()
#