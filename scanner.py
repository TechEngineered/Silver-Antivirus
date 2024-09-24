import tkinter as tk
from tkinter import filedialog, messagebox

class Scanner:
    def __init__(self):
        pass

    def scan_pc(self):
        directory = filedialog.askdirectory()
        if directory:
            messagebox.showinfo("Scan", f"Scanning directory: {directory}")
            # Implement virus signature matching logic here
        else:
            messagebox.showwarning("Scan", "No directory selected!")
