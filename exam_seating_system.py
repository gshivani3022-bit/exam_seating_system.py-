import tkinter as tk
from tkinter import ttk, messagebox
import random

class ExamSeatingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Examination Seating Arrangement System")
        self.root.geometry("1000x700")

        self.students = [
            ("KLH2024001", "Arjun", "CSE"),
            ("KLH2024002", "Priya", "ECE"),
            ("KLH2024003", "Ravi", "AIDS"),
            ("KLH2024004", "Sneha", "CSIT"),
            ("KLH2024005", "Kiran", "CSE"),
            ("KLH2024006", "Divya", "ECE")
        ]

        title = tk.Label(root, text="Smart Examination Seating System",
                         font=("Arial", 20, "bold"))
        title.pack(pady=10)

        stats = tk.Frame(root)
        stats.pack(pady=10)

        tk.Label(stats, text="Departments: 4", width=20).grid(row=0, column=0)
        tk.Label(stats, text="Students: 378", width=20).grid(row=0, column=1)
        tk.Label(stats, text="Exam Halls: 12", width=20).grid(row=0, column=2)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Generate Seating",
                  command=self.generate_seating).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Show Students",
                  command=self.show_students).pack(side=tk.LEFT, padx=5)

        self.output = tk.Text(root, height=25, width=120)
        self.output.pack(pady=10)

    def show_students(self):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "STUDENT LIST\n\n")

        for ht, name, dept in self.students:
            self.output.insert(
                tk.END,
                f"Hall Ticket: {ht} | Name: {name} | Department: {dept}\n"
            )

    def generate_seating(self):
        self.output.delete("1.0", tk.END)

        departments = ["CSE", "ECE", "AIDS", "CSIT"]
        rows = 5
        cols = 8

        self.output.insert(tk.END, "SEATING ARRANGEMENT\n\n")

        seat_no = 1
        for r in range(rows):
            for c in range(cols):
                dept = departments[(seat_no - 1) % len(departments)]
                self.output.insert(
                    tk.END,
                    f"Seat-{seat_no:02d} ({dept})\t"
                )
                seat_no += 1
            self.output.insert(tk.END, "\n")

        messagebox.showinfo("Success", "Seating arrangement generated successfully!")


root = tk.Tk()
app = ExamSeatingSystem(root)
root.mainloop()