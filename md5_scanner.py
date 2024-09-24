import hashlib
from tkinter import filedialog, messagebox

class MD5Scanner:
    def __init__(self):
        pass

    def scan_md5(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                messagebox.showinfo("MD5", f"MD5: {file_hash}")
        else:
            messagebox.showwarning("MD5", "No file selected!")
