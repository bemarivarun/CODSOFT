import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 8:
        password_label.config(text="Password length must be at least 8 characters")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password and Username Generator")

# Create and place widgets for password generation
password_label = tk.Label(root, text="")
password_label.pack()

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_password_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_password_button.pack()

# Predefined username
username = "Varun"
username_label = tk.Label(root, text="Username: " + username)
username_label.pack()


# Start the tkinter event loop
root.mainloop()
