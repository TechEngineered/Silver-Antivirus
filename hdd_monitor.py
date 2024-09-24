import psutil
from tkinter import messagebox

class HDDMonitor:
    def __init__(self):
        pass

    def monitor_hdd(self):
        disk_usage = psutil.disk_usage('/')
        messagebox.showinfo("HDD Monitor", f"Disk usage: {disk_usage.percent}%")
