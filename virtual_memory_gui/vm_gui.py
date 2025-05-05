import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class VirtualMemorySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Memory Simulator")

        self.frame_count = 4
        self.page_sequence = []
        self.frames = []

        self.page_table = {}
        self.pointer = 0
        self.page_faults = 0
        self.algorithm = "FIFO"
        self.last_used = {}  # For LRU
        self.algorithm_faults = {"FIFO": 0, "LRU": 0, "Optimal": 0, "MRU": 0}
        self.setup_ui()

    def setup_ui(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Page Reference String (space-separated):").grid(row=0, column=0, padx=5)
        self.entry = tk.Entry(input_frame, width=30)
        self.entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Algorithm:").grid(row=0, column=2, padx=5)
        self.algo_combo = ttk.Combobox(input_frame, values=["FIFO", "LRU", "Optimal", "MRU"], state="readonly", width=10)
        self.algo_combo.current(0)
        self.algo_combo.grid(row=0, column=3, padx=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        self.start_button = tk.Button(button_frame, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(side="left", padx=5)

        self.next_button = tk.Button(button_frame, text="Next Step", command=self.next_step, state="disabled")
        self.next_button.pack(side="left", padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_simulation)
        self.reset_button.pack(side="left", padx=5)

        self.stats_button = tk.Button(button_frame, text="Show Statistics", command=self.show_statistics)
        self.stats_button.pack(side="left", padx=5)

        self.memory_frame = tk.LabelFrame(self.root, text="Physical Memory")
        self.memory_frame.pack(pady=10)
        self.memory_labels = []
        for _ in range(self.frame_count):
            label = tk.Label(self.memory_frame, text="Empty", width=10, height=2, borderwidth=2, relief="groove", bg="white")
            label.pack(side="left", padx=5)
            self.memory_labels.append(label)

        self.page_table_view = ttk.Treeview(self.root, columns=("Page", "Frame", "Valid"), show="headings")
        self.page_table_view.heading("Page", text="Page")
        self.page_table_view.heading("Frame", text="Frame No.")
        self.page_table_view.heading("Valid", text="Valid Bit")
        self.page_table_view.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Page Faults: 0")
        self.status_label.pack(pady=5)

    def start_simulation(self):
        try:
            self.page_sequence = list(map(int, self.entry.get().strip().split()))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter space-separated integers.")
            return

        self.algorithm = self.algo_combo.get()
        self.frames = []
        self.page_table = {}
        self.pointer = 0
        self.page_faults = 0
        self.last_used = {}
        self.algorithm_faults = {"FIFO": 0, "LRU": 0, "Optimal": 0, "MRU": 0}
        self.next_button.config(state="normal")

        self.update_memory_display()
        self.update_page_table()
        self.status_label.config(text="Page Faults: 0")

    def reset_simulation(self):
        self.entry.delete(0, tk.END)
        self.frames = []
        self.page_table = {}
        self.pointer = 0
        self.page_faults = 0
        self.last_used = {}
        self.algorithm_faults = {"FIFO": 0, "LRU": 0, "Optimal": 0, "MRU": 0}
        self.next_button.config(state="disabled")
        self.update_memory_display()
        self.update_page_table()
        self.status_label.config(text="Page Faults: 0")

    def next_step(self):
        if self.pointer >= len(self.page_sequence):
            messagebox.showinfo("Done", "Simulation completed.")
            return

        current_page = self.page_sequence[self.pointer]
        self.pointer += 1
        current_time = self.pointer

        if current_page in self.page_table and self.page_table[current_page]["valid"]:
            if self.algorithm == "LRU" or self.algorithm == "MRU":
                self.last_used[current_page] = current_time
        else:
            self.page_faults += 1
            if len(self.frames) >= self.frame_count:
                evict = self.select_victim(current_time)
                self.frames.remove(evict)
                self.page_table[evict]["valid"] = False
                if evict in self.last_used:
                    del self.last_used[evict]

            self.frames.append(current_page)
            self.page_table[current_page] = {"frame": self.frames.index(current_page), "valid": True}
            if self.algorithm == "LRU" or self.algorithm == "MRU":
                self.last_used[current_page] = current_time

        self.update_memory_display()
        self.update_page_table()
        self.status_label.config(text=f"Page Faults: {self.page_faults}")
        self.algorithm_faults[self.algorithm] = self.page_faults

    def select_victim(self, current_time):
        if self.algorithm == "FIFO":
            return self.frames[0]
        elif self.algorithm == "LRU":
            return min(self.last_used, key=self.last_used.get)
        elif self.algorithm == "Optimal":
            future = self.page_sequence[self.pointer:]
            future_indices = {frame: (future.index(frame) if frame in future else float('inf')) for frame in self.frames}
            return max(future_indices, key=future_indices.get)
        elif self.algorithm == "MRU":
            return self.frames[-1]

    def update_memory_display(self):
        for i in range(self.frame_count):
            if i < len(self.frames):
                self.memory_labels[i].config(text=f"Page {self.frames[i]}", bg="lightblue")
            else:
                self.memory_labels[i].config(text="Empty", bg="white")

    def update_page_table(self):
        for item in self.page_table_view.get_children():
            self.page_table_view.delete(item)

        for page, info in sorted(self.page_table.items()):
            frame = info["frame"] if info["valid"] else "-"
            valid = "1" if info["valid"] else "0"
            self.page_table_view.insert("", "end", values=(page, frame, valid))

    def show_statistics(self):
        stat_window = tk.Toplevel(self.root)
        stat_window.title("Page Fault Statistics")

        # Display Page Faults
        tk.Label(stat_window, text="Page Faults for each algorithm:").pack(pady=10)
        stats_text = "\n".join([f"{algo}: {self.algorithm_faults[algo]}" for algo in self.algorithm_faults])
        tk.Label(stat_window, text=stats_text).pack(pady=10)

        # Show graph
        self.plot_statistics(stat_window)

    def plot_statistics(self, stat_window):
        # Prepare Data
        algorithms = list(self.algorithm_faults.keys())
        faults = list(self.algorithm_faults.values())

        # Create a Figure
        fig, ax = plt.subplots()
        
        # Clear previous plots before drawing new one
        ax.clear()
        
        # Create Bar Plot
        ax.bar(algorithms, faults, color=['blue', 'green', 'red', 'orange'])

        ax.set_title('Comparison of Page Faults for Different Algorithms')
        ax.set_xlabel('Algorithms')
        ax.set_ylabel('Page Faults')

        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=stat_window)
        canvas.draw()
        canvas.get_tk_widget().pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualMemorySimulator(root)
    root.mainloop()
