import shutil
import tempfile
from tkinter import messagebox

class JunkCleaner:
    def __init__(self):
        pass

    def clean_junk(self):
        try:
            temp_dir = tempfile.gettempdir()
            shutil.rmtree(temp_dir)
            messagebox.showinfo("Junk Cleaner", "Temporary files cleaned!")
        except Exception as e:
            messagebox.showerror("Junk Cleaner", f"Failed to clean junk: {str(e)}")
