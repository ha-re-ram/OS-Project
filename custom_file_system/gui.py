import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from custom_fs import FileSystem  # Make sure your class is in custom_fs.py

fs = FileSystem()

def create_file():
    path = simpledialog.askstring("Create File", "Enter file path (e.g. /file1.txt):")
    if path:
        perm = simpledialog.askstring("Permissions", "Enter permissions (e.g. rwx):", initialvalue="rw")
        fs.create_file(path, permission=perm)

def write_file():
    path = simpledialog.askstring("Write File", "Enter file path to write to:")
    if path:
        data = simpledialog.askstring("Write Data", "Enter data to write:")
        if data:
            fs.write_file(path, data)

def read_file():
    path = simpledialog.askstring("Read File", "Enter file path to read:")
    if path:
        fs.read_file(path)

def delete_file():
    path = simpledialog.askstring("Delete File", "Enter file path to delete:")
    if path:
        fs.delete_file(path)

def show_usage():
    fs.disk_usage()

def dump_disk():
    output_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Disk Dump As", filetypes=[("Text Files", "*.txt")])
    if output_path:
        fs.dump_disk(output_path)
        messagebox.showinfo("Disk Dump", f"Disk contents dumped to {output_path}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Virtual File System GUI")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="📁 Virtual File System", font=("Helvetica", 16, "bold")).pack(pady=10)

buttons = [
    ("Create File", create_file),
    ("Write File", write_file),
    ("Read File", read_file),
    ("Delete File", delete_file),
    ("Disk Usage", show_usage),
    ("Dump Disk to Text File", dump_disk),
]

for text, command in buttons:
    tk.Button(frame, text=text, command=command, width=30, pady=5).pack(pady=2)

tk.Button(frame, text="Exit", command=root.quit, width=30, pady=5, fg="white", bg="red").pack(pady=10)

root.mainloop()
