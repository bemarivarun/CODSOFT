import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D To-Do List")
        self.tasks = []

        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        self.add_button.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, font=("Helvetica", 12))
        self.update_button.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, font=("Helvetica", 12))
        self.remove_button.pack()

        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), selectbackground="#4CAF50", selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = self.task_entry.get()
            self.tasks[index] = new_task
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Updated", f"Task updated.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_task = self.tasks.pop(index)
            self.update_listbox()
            messagebox.showinfo("Removed", f"Task '{removed_task}' removed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

