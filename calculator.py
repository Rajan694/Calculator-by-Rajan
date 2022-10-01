import tkinter as tk
from tkinter import *
import os
import sys
calc = ""

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def addcalc(symbol):
    global calc
    calc += str(symbol)
    testres.delete(1.0, "end")
    testres.insert(1.0, calc)


def cutcal():
    global calc
    calc = calc[:-1]
    testres.delete(1.0, "end")
    testres.insert(1.0, calc)


def evalcalc():
    global calc
    try:
        calc = str(eval(calc))
        testres.delete(1.0, "end")
        testres.insert(1.0, calc)
    except:
        clear()
        testres.insert(1.0, "Error")


def clear():
    global calc
    calc = ""
    testres.delete(1.0, "end")


root = Tk()
root.geometry("292x278")
root.resizable(False, False)
root.title("My Calculator")
raj=resource_path("calc.ico")
root.iconbitmap(raj)
root.configure(bg="#17161b")
testres = tk.Text(root, width=16, height=2, font=("Arial bold", 24))
testres.grid(columnspan=5)

b1 = tk.Button(root, text="1", command=lambda: addcalc(1), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b1.grid(row=5, column=1)
b2 = tk.Button(root, text="2", command=lambda: addcalc(2), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b2.grid(row=5, column=2)
b3 = tk.Button(root, text="3", command=lambda: addcalc(3), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b3.grid(row=5, column=3)
b4 = tk.Button(root, text="4", command=lambda: addcalc(4), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b4.grid(row=4, column=1)
b5 = tk.Button(root, text="5", command=lambda: addcalc(5), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b5.grid(row=4, column=2)
b6 = tk.Button(root, text="6", command=lambda: addcalc(6), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b6.grid(row=4, column=3)
b7 = tk.Button(root, text="7", command=lambda: addcalc(7), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b7.grid(row=3, column=1)
b8 = tk.Button(root, text="8", command=lambda: addcalc(8), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b8.grid(row=3, column=2)
b9 = tk.Button(root, text="9", command=lambda: addcalc(9), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b9.grid(row=3, column=3)
bdot = tk.Button(root, text=".", command=lambda: addcalc("."), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
                 bg="#2a2d36")
bdot.grid(row=2, column=3)
b0 = tk.Button(root, text="0", command=lambda: addcalc(0), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
               bg="#2a2d36")
b0.grid(row=6, column=2)
bplus = tk.Button(root, text="+", command=lambda: addcalc("+"), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
                  bg="#2a2d36")
bplus.grid(row=5, column=4)
bminus = tk.Button(root, text="-", command=lambda: addcalc("-"), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
                   bg="#2a2d36")
bminus.grid(row=4, column=4)
bmul = tk.Button(root, text="*", command=lambda: addcalc("*"), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
                 bg="#2a2d36")
bmul.grid(row=3, column=4)
bdiv = tk.Button(root, text="/", command=lambda: addcalc("/"), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
                 bg="#2a2d36")
bdiv.grid(row=2, column=4)
bstb = tk.Button(root, text="(", command=lambda: addcalc("("), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
                 bg="#2a2d36")
bstb.grid(row=6, column=1)
bendb = tk.Button(root, text=")", command=lambda: addcalc(")"), width=5, font=("Arial bold", 16), bd=1, fg="#fff",
                  bg="#2a2d36")
bendb.grid(row=6, column=3)
bclear = tk.Button(root, text="C", command=clear, width=5, font=("Arial bold", 16), bd=1, fg="#fff", bg="#3697f5")
bclear.grid(row=2, column=1)
bequal = tk.Button(root, text="=", command=evalcalc, width=5, font=("Arial bold", 16), bd=1, fg="#fff", bg="#fe9037")
bequal.grid(row=6, column=4)
bcut = tk.Button(root, text="X", command=cutcal, width=5, font=("Arial bold", 16), bd=1, fg="#2a2d36", bg="#fff")
bcut.grid(row=2, column=2)

root.mainloop()
