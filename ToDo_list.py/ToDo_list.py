import tkinter as tk

root = tk.Tk()
root.title("To-Do List")

tasks = []

def add_task():
    
    task_text = entry.get()
    if task_text:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(frame, text=task_text, variable=var)
        cb.pack(anchor="w")
        tasks.append((cb, var))
        entry.delete(0, tk.END)

def delete_completed():
    for cb, var in tasks[:]:
        if var.get():
            cb.destroy()
            tasks.remove((cb, var))

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

del_btn = tk.Button(root, text="Delete Completed", command=delete_completed)
del_btn.pack(pady=5)

root.mainloop()
