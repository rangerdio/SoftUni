import tkinter as tk

def button_click():
    label.config(text="Button was clicked!")

root = tk.Tk()
root.title("Simple GUI App")

button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
