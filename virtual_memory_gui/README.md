# 🧠 Virtual Memory Management Simulator (GUI-Based)

This part of the OS Lab Project is a **GUI-based educational tool** that visually illustrates how virtual memory is managed in an operating system using different **page replacement algorithms**. It is built using **Python** and **Tkinter**, with **matplotlib** for graphical statistics.

---

## 🎯 Objective

To help students understand virtual memory concepts and page replacement mechanisms like:
- FIFO (First-In-First-Out)
- LRU (Least Recently Used)
- Optimal
- MRU (Most Recently Used)

This tool simulates the memory access process and displays how pages are loaded into physical frames, with visual feedback and page fault tracking.

---

## 📸 Features

- Input any page reference string.
- Select one of four algorithms: **FIFO**, **LRU**, **Optimal**, **MRU**.
- **Step-by-step simulation** of memory allocation and page replacement.
- Real-time **Page Table View** and **Physical Memory Frame Visualization**.
- **Page fault counter** with live updates.
- **Statistics window** comparing total page faults across all algorithms using a **bar graph**.

---

## 📁 File Structure

```bash
virtual_memory_gui/
├── vm_gui.py           # Main GUI simulator script
├── assets/             # Optional folder for icons/images (currently empty)
└── README.md           # This file
```

---

## ▶️ How to Run

### 📌 Requirements

- Python 3.x
- tkinter (usually comes with Python)
- matplotlib

### 🔧 Install matplotlib (if not installed)
```bash
pip install matplotlib
```

### 🚀 Run the Simulator
```bash
python vm_gui.py
```
---

## 🧪 How to Use

- **Enter a Page Reference String** `(e.g., 7 0 1 2 0 3 0 4 2 3 0 3 2)`.
- **Choose an Algorithm** from the dropdown.
- Click **Start Simulation** to initialize.
- Click **Next Step** to simulate memory access one page at a time.
- View the **Physical Memory** and **Page Table** updating live.
- Use **Show Statistics** to compare total page faults across all algorithms.
- Use **Reset** to start a new simulation.

---

## 📊 Sample Output

- Memory frames update visually with `page numbers` and `color changes`.
- `Page table` reflects which `page` is in which `frame` and the valid `bit`.
- `Page faults` are counted and displayed.
- A statistics window shows a comparison graph of page faults for `FIFO`, `LRU`, `Optimal`, and `MRU`.

--- 

## 📚 Learning Outcome

- This tool strengthens conceptual understanding of:

- Page faults

- Frame allocation

- Memory access patterns

- How various page replacement algorithms work

---

## 🤝 Contribution

This simulator is built for educational purposes. Contributions and improvements are welcome through pull requests or issues.

