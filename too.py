import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import tkinter as tk  
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")


app = ttk.Window(themename="flatly")  
app.title("📝 To-Do List")
app.geometry("400x450")
app.resizable(False, False)

task_entry = ttk.Entry(app, width=40)
task_entry.pack(pady=15)


btn_frame = ttk.Frame(app)
btn_frame.pack(pady=5)

add_btn = ttk.Button(btn_frame, text="Add Task", command=add_task, bootstyle="success")
add_btn.grid(row=0, column=0, padx=5)

del_btn = ttk.Button(btn_frame, text="Delete Task", command=delete_task, bootstyle="danger")
del_btn.grid(row=0, column=1, padx=5)

save_btn = ttk.Button(btn_frame, text="Save Tasks", command=save_tasks, bootstyle="info")
save_btn.grid(row=0, column=2, padx=5)


task_listbox = tk.Listbox(app, width=50, height=15, bg="white", fg="black", font=("Segoe UI", 11))
task_listbox.pack(pady=10)


load_tasks()

app.mainloop()
