import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.canvas = tk.Canvas(self.frame)
        self.task_frame = tk.Frame(self.canvas)
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left")
        self.canvas.create_window((0,0), window=self.task_frame, anchor="nw")
        
        self.task_frame.bind("<Configure>", self.on_frame_configure)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        self.add_task_button = tk.Button(self.root, text="Add Task", width=48, command=self.add_task)
        self.add_task_button.pack()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_task(self):
        task_text = self.entry.get()
        if task_text != "":
            self.tasks.append(task_text)
            self.update_tasks()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self, index):
        self.tasks.pop(index)
        self.update_tasks()

    def toggle_task(self, index):
        if self.task_checkboxes[index].var.get():
            self.task_labels[index].config(fg="grey")
        else:
            self.task_labels[index].config(fg="black")

    def update_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        self.task_checkboxes = []
        self.task_labels = []

        for index, task in enumerate(self.tasks):
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.task_frame, variable=var, command=lambda idx=index: self.toggle_task(idx))
            checkbox.var = var
            checkbox.grid(row=index, column=0, sticky='w')
            self.task_checkboxes.append(checkbox)

            label = tk.Label(self.task_frame, text=task, width=40, anchor="w")
            label.grid(row=index, column=1, sticky='w')
            self.task_labels.append(label)

            delete_button = tk.Button(self.task_frame, text="Delete", command=lambda idx=index: self.delete_task(idx))
            delete_button.grid(row=index, column=2, sticky='w')

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
