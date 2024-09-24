import tkinter as tk
from tkinter import PhotoImage
from scanner import Scanner
from updater import Updater
from junk_cleaner import JunkCleaner
from hdd_monitor import HDDMonitor
from md5_scanner import MD5Scanner
from PIL import Image, ImageTk

class SilverAntivirus:
    def __init__(self, root):
        self.root = root
        self.root.title("Silver Antivirus")
        self.root.geometry("500x400")  # Increased height to fit the image

        # Set the window icon
        icon_image = ImageTk.PhotoImage(file="logo.ico")  # Replace with the correct image path
        self.root.iconphoto(False, icon_image)  # Set the window icon to your logo

        # Add the logo image
        image = Image.open("logo.png")  # Open the image using Pillow
        resized_image = image.resize((100, 100))  # Resize to desired dimensions (width, height)
        self.logo_image = ImageTk.PhotoImage(resized_image)  # Convert to PhotoImage
        logo_label = tk.Label(self.root, image=self.logo_image)
        logo_label.pack(pady=10)

        # Add UI components
        label = tk.Label(self.root, text="Silver Antivirus", font=("Arial", 24))
        label.pack(pady=10)

        tagline = tk.Label(self.root, text="Protect Your PC", font=("Arial", 14), fg="red")
        tagline.pack()

        # Initialize classes
        self.scanner = Scanner()
        self.updater = Updater()
        self.junk_cleaner = JunkCleaner()
        self.hdd_monitor = HDDMonitor()
        self.md5_scanner = MD5Scanner()

        # Buttons
        buttons = [
            ("Scan Your PC", self.scanner.scan_pc),
            ("Update", self.updater.update_av),
            ("Junk Cleaner", self.junk_cleaner.clean_junk),
            ("HDD Monitor", self.hdd_monitor.monitor_hdd),
            ("Scan For MD5 (Advanced)", self.md5_scanner.scan_md5),
            ("Exit", self.root.quit)
        ]

        for (text, func) in buttons:
            btn = tk.Button(self.root, text=text, command=func, width=20)
            btn.pack(pady=5)

# Entry point for the program
if __name__ == "__main__":
    root = tk.Tk()
    app = SilverAntivirus(root)
    root.mainloop()
