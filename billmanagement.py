from tkinter import *

root = Tk()
root.geometry("1100x500")
root.title("Bill management")
root.resizable(False, False)

# Reset function to clear all entry fields
def Reset():
    entry_dosa.delete(0, END)
    entry_idli.delete(0, END)
    entry_pori.delete(0, END)
    entry_tea.delete(0, END)
    entry_coffee.delete(0, END)
    entry_eggs.delete(0, END)

# Function to calculate the total bill
def Total():
    try:
        a1 = int(dosa.get())
    except:
        a1 = 0

    try:
        a2 = int(idli.get())
    except:
        a2 = 0

    try:
        a3 = int(pori.get())
    except:
        a3 = 0

    try:
        a4 = int(tea.get())
    except:
        a4 = 0

    try:
        a5 = int(coffee.get())
    except:
        a5 = 0

    try:
        a6 = int(eggs.get())
    except:
        a6 = 0

    # Cost for each item per single unit
    c1 = 30 * a1
    c2 = 15 * a2
    c3 = 60 * a3
    c4 = 10 * a4
    c5 = 15 * a5
    c6 = 7 * a6

    total_cost = c1 + c2 + c3 + c4 + c5 + c6
    total_bill = f"Rs. {total_cost:.2f}"
    Total_bill.set(total_bill)

    lbl_total = Label(f2, font=(30), text="Total", width=10, fg="yellow", bg="black")
    lbl_total.place(x=0, y=50)

    entry_total = Entry(f2, font=(20), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
    entry_total.place(x=20, y=100)

# Title label
Label(text="Bill Management", bg="grey", fg="black", font=(33), width="200", height="3").pack()

# Main menu card
f = Frame(root, bg="lightblue", highlightbackground="white", highlightthickness=1, width=300, height=370)
f.place(x=10, y=81)

Label(f, text="Menu", font=(40), fg="black", bg="white").place(x=80, y=0)

Label(f, font=(17), text="Dosa.......RS.30/plate", fg="black", bg="white").place(x=10, y=80)
Label(f, font=(17), text="Idli.......RS.15/plate", fg="black", bg="white").place(x=10, y=120)
Label(f, font=(17), text="Pori.......RS.60/plate", fg="black", bg="white").place(x=10, y=160)
Label(f, font=(17), text="Tea.......RS.10/plate", fg="black", bg="white").place(x=10, y=200)
Label(f, font=(17), text="Coffee.......RS.15/plate", fg="black", bg="white").place(x=10, y=240)
Label(f, font=(17), text="Eggs.......RS.7/plate", fg="black", bg="white").place(x=10, y=280)

# Bill frame
f2 = Frame(root, bg="lightyellow", highlightbackground="black", width=300, height=370)
f2.place(x=690, y=81)

Bill = Label(f2, text="Bill", font=20, bg="lightyellow")
Bill.place(x=120, y=2)

# Entry work
f1 = Frame(root, bd=5, height=300, width=370, relief=RAISED)
f1.pack()

# Variables
dosa = StringVar()
idli = StringVar()
pori = StringVar()
tea = StringVar()
coffee = StringVar()
eggs = StringVar()
Total_bill = StringVar()

# Labels and entries for items
lbl_dosa = Label(f1, font=20, text="Dosa", width=12, fg="blue4")
lbl_idli = Label(f1, font=20, text="Idli", width=12, fg="blue4")
lbl_pori = Label(f1, font=20, text="Pori", width=12, fg="blue4")
lbl_tea = Label(f1, font=20, text="Tea", width=12, fg="blue4")
lbl_coffee = Label(f1, font=20, text="Coffee", width=12, fg="blue4")
lbl_eggs = Label(f1, font=20, text="Eggs", width=12, fg="blue4")

lbl_dosa.grid(row=1, column=0)
lbl_idli.grid(row=2, column=0)
lbl_pori.grid(row=3, column=0)
lbl_tea.grid(row=4, column=0)
lbl_coffee.grid(row=5, column=0)
lbl_eggs.grid(row=6, column=0)

# Entry widgets
entry_dosa = Entry(f1, font=20, textvariable=dosa, bd=6, width=8, bg="lightpink")
entry_idli = Entry(f1, font=20, textvariable=idli, bd=6, width=8, bg="lightpink")
entry_pori = Entry(f1, font=20, textvariable=pori, bd=6, width=8, bg="lightpink")
entry_tea = Entry(f1, font=20, textvariable=tea, bd=6, width=8, bg="lightpink")
entry_coffee = Entry(f1, font=20, textvariable=coffee, bd=6, width=8, bg="lightpink")
entry_eggs = Entry(f1, font=20, textvariable=eggs, bd=6, width=8, bg="lightpink")

entry_dosa.grid(row=1, column=1)
entry_idli.grid(row=2, column=1)
entry_pori.grid(row=3, column=1)
entry_tea.grid(row=4, column=1)
entry_coffee.grid(row=5, column=1)
entry_eggs.grid(row=6, column=1)

# Buttons
btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=16, width=10, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="lightblue", font=16, width=10, text="Total", command=Total)
btn_total.grid(row=8, column=1)

root.mainloop()
