import datetime
import tkinter as tk
from tkinter import ttk

date = ""


def get_attendance(root):
    from db import print_table
    global date

    popup = tk.Toplevel(root)

    popup.title("Display attendance")
    popup.geometry("1000x700")
    popup.grid_rowconfigure(0, weight=1)
    popup.grid_columnconfigure(0, weight=1)

    from utils import title_bar_mode
    from utils import theme
    title_bar_mode(popup, theme)

    frame1 = ttk.LabelFrame(popup, text=f"Attendance for {date}", style='Card.TFrame', padding=(20, 20, 20, 20))
    frame1.place(relx=0, rely=0, relwidth=1, relheight=1)  # use place and relative coordinates for the parent frame

    name_frame = ttk.LabelFrame(frame1, text="Name", style='Card.TFrame', padding=(10, 10, 10, 10))
    name_frame.place(relx=0, rely=0, relwidth=0.2,
                     relheight=0.9)  # use place and relative width and height for the child frames

    class_frame = ttk.LabelFrame(frame1, text="Class", style='Card.TFrame', padding=(10, 10, 10, 10))
    class_frame.place(relx=0.2, rely=0, relwidth=0.2, relheight=0.9)

    sec_frame = ttk.LabelFrame(frame1, text="Section", style='Card.TFrame', padding=(10, 10, 10, 10))
    sec_frame.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.9)

    rnum_frame = ttk.LabelFrame(frame1, text="Roll No.", style='Card.TFrame', padding=(10, 10, 10, 10))
    rnum_frame.place(relx=0.6, rely=0, relwidth=0.2, relheight=0.9)

    cc_frame = ttk.LabelFrame(frame1, text="CC", style='Card.TFrame', padding=(10, 10, 10, 10))
    cc_frame.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.9)

    frames = [name_frame, class_frame, sec_frame, rnum_frame, cc_frame]

    print_table(popup, frames, date)

    if popup.winfo_exists():
        from utils import main_window
        home_btn = ttk.Button(frame1, padding=(10, 10, 10, 10), text="Return to main menu",
                              command=lambda: (popup.destroy(), main_window(root)))
        home_btn.place(relx=0.4, rely=0.92)  # use place and relative coordinates for the button as well


def get_date(root, txt, popup):
    global date
    date = txt.get()
    popup.destroy()
    print(f"Attendance req for date: {date}")
    get_attendance(root)


def date_today(root):
    global date
    today = datetime.date.today()
    date = today.strftime('%d-%m-%y')
    print(f"Attendance req for date: {date}")
    get_attendance(root)


def ask_date(root):
    popup = tk.Toplevel(root)

    popup.title("Display attendance")
    popup.geometry("500x300")
    popup.resizable(False, False)
    popup.grid_rowconfigure(0, weight=1)
    popup.grid_columnconfigure(0, weight=1)

    from utils import title_bar_mode
    from utils import theme
    title_bar_mode(popup, theme)

    frame = ttk.LabelFrame(popup, text="Choose a date", style='Card.TFrame', padding=(15, 7, 15, 15))
    frame.grid(column=0, row=0)

    text = ttk.Entry(frame, width=23)
    text.grid(column=1, row=0, pady=7)

    button = ttk.Button(frame, width=20, text="Submit", style='Accent.TButton',
                        command=lambda: get_date(root, text, popup))
    button.grid(column=0, row=1, columnspan=2, pady=7)


def display_attendance(root):
    from utils import clear_window, main_window

    clear_window(root)

    frame = ttk.LabelFrame(root, text="Display attendance", style='Card.TFrame', padding=(15, 7, 15, 15))
    frame.grid(column=0, row=0)

    btn1 = ttk.Button(frame, width=20, text="Today's attendance", style='Accent.TButton',
                      command=lambda: date_today(root))
    btn1.grid(column=0, row=1, pady=7)
    btn2 = ttk.Button(frame, width=20, text="Choose a date", command=lambda: ask_date(root))
    btn2.grid(column=0, row=2, pady=7)
    btn3 = ttk.Button(frame, width=20, text="Return to main menu", command=lambda: main_window(root))
    btn3.grid(column=0, row=3, pady=7)
