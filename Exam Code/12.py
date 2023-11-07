import tkinter as tk

def toggle():
    if int_var.get() == 1:
        label.config(text="Selected")
    else:
        label.config(text="Not Selected")

root = tk.Tk()
root.title("IntVar Example")

int_var = tk.IntVar()

checkbutton = tk.Checkbutton(root, text="Check Me", variable=int_var, command=toggle)
label = tk.Label(root, text="")

checkbutton.pack()
label.pack()

root.mainloop()
