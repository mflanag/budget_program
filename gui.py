import tkinter as tk
from tkinter import ttk

# Global Objects
top = tk.Tk()
cost = None
update_btn = None
style = ttk.Style()

ctgory = ''

def update_db():
    # check that there is valid info selected
    if ctgory == '' or cost.getdouble() <= 0.0:
        # display an error
        pass
    #
    # update the database
    print("Categories updated %s")
    # update the button to show good
    update_btn.configure(text="Database Updated")
    # clear variables
    ctgory = ''
    cost.delete(0, -1)

#

# categories needs to be pulled from the database
def init_GUI(categories):
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
        col += 1
        if col % 3 == 0:
            col = 0
            row += 1
        #
    #

    # set locations
    end_col = int(len(categories) / 3)
    cat_lbl.grid(column=0, row=0, columnspan=(end_col+1))
    cost.grid(column=(end_col + 1), row=1)
    cost_lbl.grid(column=(end_col+1), row=0)
    update_btn.grid(column=(end_col + 2), row=1)
#

def run_GUI():
    top.mainloop()
#

cat_lbl = tk.Label(top, text="Select a Category Below", font=("Arial Bold", 24))
cost_lbl = tk.Label(top, text="Enter Cost Below", font=("Arial", 10))
cost = tk.Entry(top, text="Cost")
update_btn = tk.Button(top, text="Enter Record", bg="white", fg="black", command=update_db)

if __name__ == "__main__":
    init_GUI(['Groceries', 'Electronics', 'Gas', 'Dining', 'Bars', 'Entertainment', 'Subscriptions', 'Rent', 'Physical', 'Utilities', \
        'Car', 'Motorcycle', 'Insurance', 'Vacation', 'Books', 'Bicycle'])
    run_GUI()
#