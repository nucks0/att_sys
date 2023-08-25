import tkinter as tk
import sv_ttk
from utils import main_window

# Blurry text fix caused due to scaling
# https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# import os
# os.environ['SV_TTK_PATH'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sv_ttk')

# Create the main root
root = tk.Tk()
# photo = tk.PhotoImage(file="C:/Users/c2409/PycharmProjects/pythonProject4/attendanceapp.png")
photo = tk.PhotoImage(file="attendanceapp.png")
root.iconphoto(True, photo)

root.geometry("800x500")
root.resizable(False, False)
root.title("Attendance Tracker")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_window(root)

# Start the main loop
root.mainloop()

