import tkinter as tk

master = tk.Tk()
tk.Label(master, text="Office").grid(row=0, column= 0, columnspan = 1)
tk.Entry(master).grid(row=0, column = 1, columnspan = 8, ipadx = 400)


e1 = tk.Entry(master)
e2 = tk.Entry(master)


def on_enter(event):
    # Change button color when mouse enters
    event.widget.config(bg="lightblue")

def on_leave(event):
    # Revert button color when mouse leaves
    event.widget.config(bg="SystemButtonFace")


# Rileva il valore
string= e1.get()
print()

# Numer of rows
rows = 14 
Table = [None] * rows

# Numer of Columns
columns= 10

for n in range(len(Table)):
    Table [n] = [None] * columns

print(len(Table))
print(Table)

for n in range(rows):
    tk.Entry(master).grid(row=n+1, column=0)
    for i in range(columns):
        Table[n][i] = tk.Entry(master)
        Table[n][i].grid(row=n+1, column=i)
        Table[n][i].bind("<Enter>", on_enter)
        Table[n][i].bind("<Leave>", on_leave)
        print("Numer"+ str(i))
    print(n)
print("TABLE" + str(Table[0][0].get()))


def print_table():
    for el in Table:
        print("VALUE IS" + str(el[0].get()))


A = tk.Button(master, text = "D", command = print_table)
A.grid(row=20, column=0)


# Bind hover events to the button
B = A.bind("<Enter>", on_enter)
C = A.bind("<Leave>", on_leave)

print("B" +str(B))

def update_position():
    for n in range(rows):
        for i in range(columns):
            print("Numer"+ str(Table[n][i].get()))
            pass
    master.after(1000,update_position)


master.after(1000,update_position)

master.mainloop()



