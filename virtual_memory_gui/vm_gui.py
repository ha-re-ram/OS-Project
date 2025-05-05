import tkinter as tk
from tkinter import ttk, messagebox

class VirtualMemorySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Memory Management Simulator")

        self.frame_count = 4
        self.page_sequence = []
        self.frames = []
        self.page_table = {}
        self.pointer = 0
        self.algorithm = "FIFO"
        self.page_faults = 0
        self.history = []
        self.setup_ui()

    def setup_ui(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        tk.Label(top_frame, text="Page Reference String (space-separated):").grid(row=0, column=0, padx=5)
        self.entry = tk.Entry(top_frame, width=40)
        self.entry.grid(row=0, column=1, padx=5)

        tk.Label(top_frame, text="Algorithm:").grid(row=0, column=2, padx=5)
        self.algo_combo = ttk.Combobox(top_frame, values=["FIFO", "LRU"], state="readonly")
        self.algo_combo.current(0)
        self.algo_combo.grid(row=0, column=3, padx=5)

        tk.Button(self.root, text="Start Simulation", command=self.start_simulation).pack(pady=5)
        tk.Button(self.root, text="Next Step", command=self.next_step).pack(pady=5)
        tk.Button(self.root, text="Reset", command=self.reset_simulation).pack(pady=5)

        self.memory_frame = tk.LabelFrame(self.root, text="Physical Memory")
        self.memory_frame.pack(pady=10)
        self.memory_labels = [tk.Label(self.memory_frame, text="Empty", width=10, height=2, borderwidth=2, relief="groove")
                              for _ in range(self.frame_count)]
        for label in self.memory_labels:
            label.pack(side="left", padx=5)

        self.page_table_frame = ttk.Treeview(self.root, columns=("Page", "Frame", "Valid"), show="headings")
        self.page_table_frame.heading("Page", text="Page")
        self.page_table_frame.heading("Frame", text="Frame No.")
        self.page_table_frame.heading("Valid", text="Valid Bit")
        self.page_table_frame.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Page Faults: 0")
        self.status_label.pack(pady=5)

    def start_simulation(self):
        self.page_sequence = list(map(int, self.entry.get().strip().split()))
        self.algorithm = self.algo_combo.get()
        self.frames.clear()
        self.page_table.clear()
        self.pointer = 0
        self.page_faults = 0
        self.history.clear()

        for label in self.memory_labels:
            label.config(text="Empty", bg="white")
        for item in self.page_table_frame.get_children():
            self.page_table_frame.delete(item)
        self.status_label.config(text="Page Faults: 0")

    def reset_simulation(self):
        self.entry.delete(0, tk.END)
        self.start_simulation()

    def next_step(self):
        if self.pointer >= len(self.page_sequence):
            messagebox.showinfo("Done", "Simulation completed.")
            return

        current_page = self.page_sequence[self.pointer]
        self.pointer += 1

        in_memory = current_page in self.page_table and self.page_table[current_page]['valid']

        if in_memory:
            if self.algorithm == "LRU":
                self.frames.remove(current_page)
                self.frames.append(current_page)
        else:
            self.page_faults += 1
            if len(self.frames) >= self.frame_count:
                evicted = self.frames.pop(0)
                self.page_table[evicted]['valid'] = False
            self.frames.append(current_page)
            self.page_table[current_page] = {'frame': self.frames.index(current_page), 'valid': True}

        self.update_memory_display()
        self.update_page_table()
        self.status_label.config(text=f"Page Faults: {self.page_faults}")

    def update_memory_display(self):
        for i in range(self.frame_count):
            if i < len(self.frames):
                self.memory_labels[i].config(text=f"Page {self.frames[i]}", bg="lightgreen")
            else:
                self.memory_labels[i].config(text="Empty", bg="white")

    def update_page_table(self):
        for item in self.page_table_frame.get_children():
            self.page_table_frame.delete(item)
        for page, info in self.page_table.items():
            frame = info['frame'] if info['valid'] else "-"
            valid = "1" if info['valid'] else "0"
            self.page_table_frame.insert("", "end", values=(page, frame, valid))

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualMemorySimulator(root)
    root.mainloop()
