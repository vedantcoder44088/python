import tkinter as tk
from PIL import Image, ImageTk

# Creating the main window
root = tk.Tk()
root.geometry('400x400')
root.title('Display Image')

# Open and display the image
image_path = "example_image.jpg"  # Replace with your own image path
img = Image.open(image_path)
img = img.resize((300, 300), Image.ANTIALIAS)  # Resize the image
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=photo)
label.image = photo  # to keep a reference
label.pack(pady=10)

root.mainloop()
