# Tkinter is Python’s built-in library used to create graphical user interface (GUI) applications.

# With Tkinter, you can make programs that have:
# windows
# buttons
# labels
# text boxes
# menus

# instead of only text in the terminal.

# In simple words 🌱
# Tkinter lets you create windows and clickable apps in Python.


# import tkinter as tk

# window = tk.Tk()
# window.title("My First App")

# label = tk.Label(window, text="Hello, Tkinter!")
# label.pack()

# window.mainloop()


import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(
    root, font=("Comic Sans MS", 50, "bold"), background="yellow", foreground="black"
)


def time():
    string = strftime("%H:%M:%S %p \n %D %A")
    label.config(text=string)
    label.after(1000, time)


label.pack(anchor="center")

time()
root.mainloop()
