#import library
import tkinter as tk

#start main gui
gui = tk.Tk()
gui.title("Seowoo's calculate")
gui.configure(bg="#796F6F")

#create entrybox
entry_box = tk.Entry(gui, width=48, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=4, padx=40, pady=20)

#creat button's function
def click(number):
    current = entry_box.get()
    entry_box.delete(0, tk.END)
    entry_box.insert(0, str(current)+str(number))

def clear():
    entry_box.delete(0, tk.END)

def add():
    num1 = entry_box.get()
    global g_num1
    global g_operation
    g_operation = "add"
    g_num1 = int(num1)
    entry_box.delete(0, tk.END)

def subtract():
    num1 = entry_box.get()
    global g_num1
    global g_operation
    g_operation = "subtract"
    g_num1 = int(num1)
    entry_box.delete(0, tk.END)

def multiply():
    num1 = entry_box.get()
    global g_num1
    global g_operation
    g_operation = "multiply"
    g_num1 = int(num1)
    entry_box.delete(0, tk.END)


def divide():
    num1 = entry_box.get()
    global g_num1
    global g_operation
    g_operation = "divide"
    g_num1 = int(num1)
    entry_box.delete(0, tk.END)

def deno():
    num1 = entry_box.get()
    global g_num1
    global g_operation
    g_operation = "deno"
    g_num1 = int(num1)
    entry_box.delete(0, tk.END)

def square():
    num1 = entry_box.get()
    global g_num1
    global g_operation
    g_operation = "square"
    g_num1 = int(num1)
    entry_box.delete(0, tk.END)

def root():
    num1 = entry_box.get()
    global g_num1
    global g_operation
    g_operation = "root"
    g_num1 = int(num1)
    entry_box.delete(0, tk.END)

def sum():
    num2 = entry_box.get()
    entry_box.delete(0, tk.END)
    if g_operation == "add":
        result = g_num1 + int(num2)
        entry_box.insert(0, result)
    elif g_operation == "subtract":
        result = g_num1 - int(num2)
        entry_box.insert(0, result)
    elif g_operation == "multiply":
        result = g_num1 * int(num2)
        entry_box.insert(0, result)
    elif g_operation == "divide":
        result = g_num1 / int(num2)
        entry_box.insert(0, result)
    elif g_operation == "deno":
        result = 1 / g_num1
        entry_box.insert(0, result)
    elif g_operation == "square":
        result = g_num1 * g_num1
        entry_box.insert(0, result)
    elif g_operation == "root":
        result = g_num1 ** 0.5
        entry_box.insert(0, result)

#create button
button_1 = tk.Button(gui, text="1", padx=45, pady=15, command=lambda: click(1))
button_2 = tk.Button(gui, text="2", padx=45, pady=15, command=lambda: click(2))
button_3 = tk.Button(gui, text="3", padx=45, pady=15, command=lambda: click(3))
button_4 = tk.Button(gui, text="4", padx=45, pady=15, command=lambda: click(4))
button_5 = tk.Button(gui, text="5", padx=45, pady=15, command=lambda: click(5))
button_6 = tk.Button(gui, text="6", padx=45, pady=15, command=lambda: click(6))
button_7 = tk.Button(gui, text="7", padx=45, pady=15, command=lambda: click(7))
button_8 = tk.Button(gui, text="8", padx=45, pady=15, command=lambda: click(8))
button_9 = tk.Button(gui, text="9", padx=45, pady=15, command=lambda: click(9))
button_0 = tk.Button(gui, text="0", padx=45, pady=15, command=lambda: click(0))

button_clear = tk.Button(gui, text="C", padx=43, pady=15, command=clear)
button_sqr = tk.Button(gui, text="**", padx=44, pady=15, command=square)
button_deno = tk.Button(gui, text="1/x", padx=39, pady=15, command=deno)
button_root = tk.Button(gui, text="√", padx=44, pady=15, command=root)

button_sum = tk.Button(gui, text="=", padx=44, pady=15, command=sum)
button_add = tk.Button(gui, text="+", padx=43, pady=15, command=add)
button_subtract = tk.Button(gui, text="-", padx=45, pady=15, command=subtract)
button_multiple = tk.Button(gui, text="*", padx=45, pady=15, command=multiply)
button_divide = tk.Button(gui, text="/", padx=45, pady=15, command=divide)

#place buttons

button_deno.grid(row=1, column=0)
button_sqr.grid(row=1, column=1)
button_root.grid(row=1, column=2)
button_clear.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiple.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

button_0.grid(row=5, column=1)
button_sum.grid(row=5, column=2)
button_add.grid(row=5, column=3)


#run main gui
gui.mainloop()
