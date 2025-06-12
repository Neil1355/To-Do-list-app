import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x500")
root.configure(bg="#f4f4f4")

tasks = []

def save_tasks():
    with open("tasks.txt", "w") as f:
        for _, var, label in tasks:
            f.write(f"{label.cget('text')}||{var.get()}\n")

def load_tasks():
    
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                if "||" in line:
                    text, status = line.strip().split("||")
                    create_task(text, bool(int(status)))
    except FileNotFoundError:
        pass

def create_task(text, completed=False):
    var = tk.BooleanVar(value=completed)
    task_frame = tk.Frame(scrollable_frame, bg="white", bd=1, relief="solid")
    task_frame.pack(fill="x", pady=4, padx=5)

    label = tk.Label(task_frame, text=text, font=("Helvetica", 11), bg="white", anchor="w")
    cb = tk.Checkbutton(task_frame, variable=var, bg="white", command=save_tasks)
    cb.pack(side="left", padx=5)
    label.pack(side="left", fill="x", expand=True, padx=5, pady=6)

    def edit(event):
        entry = tk.Entry(task_frame, font=("Helvetica", 11))
        entry.insert(0, label.cget("text"))
        entry.pack(side="left", fill="x", expand=True, padx=5)
        label.pack_forget()

        def finish_edit(event=None):
            new_text = entry.get().strip()
            if new_text:
                label.config(text=new_text)
            entry.destroy()
            label.pack(side="left", fill="x", expand=True, padx=5)
            save_tasks()

        entry.bind("<Return>", finish_edit)
        entry.bind("<FocusOut>", finish_edit)
        entry.focus()

    label.bind("<Double-1>", edit)
    tasks.append((task_frame, var, label))
    save_tasks()

title = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f4f4f4")
title.pack(pady=15)

entry_frame = tk.Frame(root, bg="#f4f4f4")
entry_frame.pack(pady=5)

task_entry = tk.Entry(entry_frame, width=25, font=("Helvetica", 12))
task_entry.pack(side="left", padx=5)

def add_task():
    text = task_entry.get().strip()
    if text:
        create_task(text)
        task_entry.delete(0, tk.END)

add_btn = tk.Button(entry_frame, text="Add", command=add_task, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
add_btn.pack(side="left", padx=(0, 3))

def delete_completed():
    for frame, var, _ in tasks[:]:
        if var.get():
            frame.destroy()
            tasks.remove((frame, var, _))
    save_tasks()

delete_btn = tk.Button(entry_frame, text="Delete Completed", command=delete_completed, bg="#e53935", fg="white", font=("Helvetica", 10, "bold"))
delete_btn.pack(side="left")

canvas = tk.Canvas(root, bg="#f4f4f4", highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f4f4f4")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(fill="both", expand=True, side="left", padx=(10, 0), pady=10)
scrollbar.pack(fill="y", side="right", padx=(0, 10))

load_tasks()
root.mainloop()