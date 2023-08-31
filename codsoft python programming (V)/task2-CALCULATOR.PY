import tkinter as tk

def press_key(key):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + key)

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])

def calculate():
    try:
        result = eval(entry.get())
        clear_entry()
        entry.insert(tk.END, result)
    except Exception:
        clear_entry()
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

entry = tk.Entry(root, font=("Helvetica", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("←", 5, 1)
]

button_colors = {
    "numbers": "#e0e0e0",
    "operators": "#f0a800",
    "equals": "#f06060",
    "clear": "#606060",
    "backspace": "#606060"
}

for (text, row, col) in buttons:
    if text in "1234567890":
        button_color = button_colors["numbers"]
    elif text in "+-*/":
        button_color = button_colors["operators"]
    elif text == "=":
        button_color = button_colors["equals"]
    elif text == "C":
        button_color = button_colors["clear"]
    elif text == "←":
        button_color = button_colors["backspace"]
    else:
        button_color = "#d0d0d0"
    
    button = tk.Button(root, text=text, font=("Helvetica", 16), padx=20, pady=20, bg=button_color)
    if text == "=":
        button.config(command=calculate)
    elif text == "C":
        button.config(command=clear_entry)
    elif text == "←":
        button.config(command=backspace)
    else:
        button.config(command=lambda t=text: press_key(t))
    button.grid(row=row, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()
