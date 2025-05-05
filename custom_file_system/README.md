# 🧠 Custom File System Simulator

This project simulates a basic block-level file system using Python. It operates on a virtual disk (`disk.img`) and allows file creation, writing, reading, and deletion. A graphical interface is also included to make it easier to interact with.

---

## 📦 Features

- ✅ Simulates a block-based virtual disk
- 📁 Basic file operations: `create`, `read`, `write`, `delete`
- 🔐 File permissions support (`r`, `w`, `x`)
- 📊 Disk usage statistics (used, free, total blocks)
- 🧠 Metadata stored in `fs_metadata.json`
- 🖼️ GUI frontend built with Tkinter
- 📄 Dump disk contents into a human-readable `.txt` file

---

## 🖥️ How to Run

### CLI Version
> Uses `custom_fs.py` (or `fs_main.py`, if you kept the original name)

```bash
python custom_fs.py
```
This runs the file system with example operations like file creation, writing, reading, and deletion.

### GUI Version
> Uses gui.py

```bash
python gui.py
```
Provides a simple interactive interface for managing the virtual file system:
- Create file
- Write to file
- Read file contents
- Delete file
- View disk usage
- Dump disk to .txt for inspection

---
## 📁 Project Structure
```bash
custom_file_system/
├── custom_fs.py         # File system logic (FileSystem class)
├── gui.py               # Tkinter GUI frontend
├── disk.img             # Virtual disk image
├── fs_metadata.json     # Metadata storage
└── disk_dump.txt        # (Optional) Human-readable disk dump
```
---
## 🔍 Sample CLI Operations
```bash
fs = FileSystem()
fs.create_file("/file1.txt", "rw")
fs.write_file("/file1.txt", "Hello from the virtual FS!")
fs.read_file("/file1.txt")
fs.disk_usage()
fs.delete_file("/file1.txt")
fs.disk_usage()
```
---
## 📝 Disk Dump Preview

Use `fs.dump_disk("disk_dump.txt")` to generate a readable version of disk contents for inspection.

---

## ⚙️ Requirements

- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)

---

## 📌 Notes

- This is a simulation, not a real OS-level file system.

- The .img file is not mountable or bootable—it's used internally to store block data.

- Useful for educational purposes and understanding low-level file system logic.
---
