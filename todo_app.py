import tkinter as tk
from tkinter import messagebox

# -------------------- Main Window --------------------
root = tk.Tk()
root.title("My To-Do App")
root.geometry("420x520")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

# -------------------- Functions --------------------
def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task")


def clear_tasks():
    listbox.delete(0, tk.END)

# -------------------- UI Components --------------------

# Title Label
title = tk.Label(
    root,
    text="To-Do List",
    font=("Segoe UI", 20, "bold"),
    bg="#f4f6f8",
    fg="#2c3e50"
)
title.pack(pady=15)

# Entry Frame
entry_frame = tk.Frame(root, bg="#f4f6f8")
entry_frame.pack(pady=10)

task_entry = tk.Entry(
    entry_frame,
    width=25,
    font=("Segoe UI", 12),
    bd=2,
    relief=tk.GROOVE
)
task_entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(
    entry_frame,
    text="Add",
    width=8,
    font=("Segoe UI", 11, "bold"),
    bg="#3498db",
    fg="white",
    command=add_task
)
add_btn.grid(row=0, column=1, padx=5)

# Listbox Frame
list_frame = tk.Frame(root)
list_frame.pack(pady=15)

listbox = tk.Listbox(
    list_frame,
    width=35,
    height=12,
    font=("Segoe UI", 11),
    bd=0,
    selectbackground="#1abc9c",
    activestyle="none"
)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Button Frame
btn_frame = tk.Frame(root, bg="#f4f6f8")
btn_frame.pack(pady=20)

delete_btn = tk.Button(
    btn_frame,
    text="Delete Task",
    width=15,
    font=("Segoe UI", 11),
    bg="#e74c3c",
    fg="white",
    command=delete_task
)
delete_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    btn_frame,
    text="Clear All",
    width=15,
    font=("Segoe UI", 11),
    bg="#95a5a6",
    fg="white",
    command=clear_tasks
)
clear_btn.grid(row=0, column=1, padx=10)

# -------------------- Run App --------------------
root.mainloop()
