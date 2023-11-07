import tkinter as tk

def register():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}\nPassword: {password}")
    # You can add further logic for storing this data or any other operations here.

# Creating the main window
root = tk.Tk()
root.geometry("300x200")
root.title("Registration")

# Creating labels and entries for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Show * instead of the actual password
password_entry.pack()

# Creating the register button
register_button = tk.Button(root, text="Register", command=register)
register_button.pack(pady=10)

root.mainloop()
