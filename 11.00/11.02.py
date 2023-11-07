import tkinter as tk
from tkinter import ttk

# List of cities
cities = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Berlin', 'Rome', 'Beijing', 'Cairo', 'Moscow']

# Creating the main window
root = tk.Tk()
root.geometry('300x200')
root.title('City Selection')

# Function to get the selected city
def get_selected_city():
    selected_city = city_var.get()
    print(f'Selected city: {selected_city}')

# Creating the dropdown list
city_var = tk.StringVar()
city_dropdown = ttk.Combobox(root, textvariable=city_var, values=cities, state='readonly')
city_dropdown.pack(pady=20)

# Creating the button to get the selected city
select_button = tk.Button(root, text='Select', command=get_selected_city)
select_button.pack()

root.mainloop()
