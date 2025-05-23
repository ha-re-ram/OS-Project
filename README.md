﻿# OS Lab Project

This repository contains a three-part Operating Systems lab project that covers foundational OS concepts through practical implementation:

## 📁 Project Structure

```bash
os_lab_project/
├── kali_linux_setup/              # Part 1: Kali Linux Installation
│   └── installation_notes.md      # Notes or description of installation
│
├── virtual_memory_gui/            # Part 2: Virtual Memory Educational Tool
│   ├── vm_gui.py                  # Main GUI simulator script
│   ├── README.md                  # Documentation for the Virtual Memory GUI
│
├── custom_file_system/            # Part 3: Simulated File System
│   ├── custom_fs.py               # File system logic (FileSystem class)
│   ├── gui.py                     # Tkinter GUI frontend
│   ├── disk.img                   # Virtual disk image
│   ├── fs_metadata.json           # Metadata storage
│   ├── disk_dump.txt              # (Optional) Human-readable disk dump
│   ├── file2.txt                  # Example file for testing
│   ├── README.md                  # Documentation for the Custom File System
│   └── __pycache__/               # Compiled Python files
│
├── report.pdf                     # Optional project report
└── README.md                      # Root readme with overview
```
---

## 🧩 Projects Overview

### ✅ 1. Kali Linux OS Installation and Configuration

- **Task**: Install **Kali Linux** on a virtual machine or a physical system.
- **Goals**:
  - Understand the Linux installation process and system partitioning.
  - Perform initial system setup and configurations.
  - Gain basic system-level knowledge including file system structure, users/permissions, and common utilities.
- **Deliverable**:
  - 🎥 [Video to setup Kali Linux](https://drive.google.com/file/d/1Atwex5t65vys9Mb8JbIbLhNjgC3l60ZQ/view)


---

### ✅ 2. Virtual Memory Educational Tool

- **Description**: A GUI-based tool to visually demonstrate how virtual memory is managed in an operating system.
- **Features**:
  - Page table and frame mapping visualization
  - Page replacement algorithms (e.g., FIFO, LRU)
  - Step-by-step simulation of memory access and replacement
- **Location**: See [`virtual_memory_gui/`](./virtual_memory_gui/)

---

### ✅ 3. Custom File System

- **Description**: A simple file system implemented in Python, operating on a simulated disk (`disk.img`).
- **Features**:
  - Block-level storage and allocation
  - Hierarchical directory structure
  - File and directory operations: create, read, write, delete
  - File permission bits (Read, Write, Execute)
  - Disk usage stats (total, used, and free space)
- **Location**: See [`custom_file_system/`](./custom_file_system/)

---

## 🔄 Recent Updates

### Custom File System
- Introduced a Tkinter-based GUI for user-friendly interaction.
- Enhanced file operations with better error handling and detailed disk usage statistics.
- Added a feature to dump disk contents into a human-readable `.txt` file for inspection.

### Virtual Memory GUI
- Added support for the MRU (Most Recently Used) page replacement algorithm.
- Improved visualization of memory frames and page tables.
- Enhanced the statistics window with a bar graph comparing page faults across algorithms.

---

## 📄 Report

A `report.pdf` may be included that documents project details, screenshots, and outcomes.

---

## 🛠️ Requirements

- Python 3.x
- GUI framework (e.g., Tkinter or PyQt)
- Virtualization Software (e.g., VirtualBox or VMware)
- Kali Linux ISO (for Experiment 1)

---

## 🤝 Contributions

This project was created for academic purposes. Contributions and suggestions are welcome via issues or pull requests.

---

