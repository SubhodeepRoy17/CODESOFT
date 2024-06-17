import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(root, width=54)
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)

    def update_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Update Task", "Enter new task:")
            if new_task:
                self.tasks[task_index] = new_task
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            del self.tasks[task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
