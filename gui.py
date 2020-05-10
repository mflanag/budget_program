import tkinter as tk

top = tk.Tk()

def clicked():
    l1.configure (text="Button was clicked !!")
#

def init_GUI():
    top.title("Budget Program")

    l1 = tk.Label(top, text="hello", font=("Arial Bold", 50))
    l1.grid(column=0, row=0)

    bt = tk.Button(top, text="Enter", bg="orange", fg="green", command=clicked)
    bt.grid(column=1, row=0)
    top.geometry('350x200')

def run_GUI():
    top.mainloop()
#

if __name__ == "__main__":
    init_GUI()
    run_GUI()