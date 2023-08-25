from datetime import date
import tkinter as tk
from tkinter import ttk

from db import Database

cc = ""
cls = ""
rnum = ""
sec = ""


def cc_attendance(txt1):
    global cc
    cc = txt1.get()
    mydb = Database()
    s = mydb.cc_fetch_student(cc)

    if s is not None:
        today = date.today()
        date_str = today.strftime('%d-%m-%y')
        mydb.add_entry(s, date_str)

        tk.messagebox.showinfo(
            title="Success!",
            message=f"Attendance marked for student: {s.cc} on {date_str}"
        )

    # Clean the text fields
    txt1.delete(0, tk.END)


def manual_attendance(txt1, txt2, txt3):
    global cls, sec, rnum
    cls = txt1.get()
    sec = txt2.get()
    rnum = txt3.get()

    mydb = Database()
    s = mydb.manual_fetch_student(cls, sec, rnum)

    if s is not None:
        today = date.today()
        date_str = today.strftime('%d-%m-%y')
        mydb.add_entry(s, date_str)

        tk.messagebox.showinfo(
            title="Success!",
            message=f"Attendance marked for student: {s.cc} on {date_str}"
        )

    # Clean the text fields
    txt1.delete(0, tk.END)
    txt2.delete(0, tk.END)
    txt3.delete(0, tk.END)


def manual_details(root):
    from utils import clear_window, main_window
    clear_window(root)

    frame = ttk.LabelFrame(root, text="Manual attendance", style='Card.TFrame', padding=(15, 7, 15, 15))
    frame.grid(column=0, row=0)

    lbl1 = ttk.Label(frame, text="Class: ")
    lbl1.grid(column=0, row=1, pady=7, padx=5)
    txt1 = ttk.Entry(frame, width=15)
    txt1.grid(column=1, row=1, pady=7)

    lbl2 = ttk.Label(frame, text="Sec: ")
    lbl2.grid(column=0, row=2, pady=7, padx=5)
    txt2 = ttk.Entry(frame, width=15)
    txt2.grid(column=1, row=2, pady=7)

    lbl3 = ttk.Label(frame, text="Roll No: ")
    lbl3.grid(column=0, row=3, pady=7, padx=5)
    txt3 = ttk.Entry(frame, width=15)
    txt3.grid(column=1, row=3, pady=7)

    submit_btn = ttk.Button(frame, text="Submit", width=20, style='Accent.TButton', command=lambda: manual_attendance(
        txt1, txt2, txt3))
    submit_btn.grid(column=0, row=5, columnspan=2, pady=7)
    home_btn = ttk.Button(frame, text="Return to main menu", width=20, command=lambda: main_window(root))
    home_btn.grid(column=0, row=6, columnspan=2, pady=7)


def take_attendance(root):
    from utils import clear_window, main_window
    clear_window(root)

    frame = ttk.LabelFrame(root, text="Mark attendance", style='Card.TFrame', padding=(15,7,15,15))
    frame.grid(column=0, row=0)

    lbl2 = ttk.Label(frame, text="Computer code:")
    lbl2.grid(column=0, row=1, pady=7, padx=5)
    txt1 = ttk.Entry(frame, width=15)
    txt1.grid(column=1, row=1, pady=7, padx=5)

    submit_btn = ttk.Button(frame, text="Submit", width=20, style='Accent.TButton', command=lambda: cc_attendance(txt1))
    submit_btn.grid(column=0, row=2, pady=7, columnspan=2)
    manual_btn = ttk.Button(frame, text="Enter details manually", width=20, command=lambda: manual_details(root))
    manual_btn.grid(column=0, row=3, pady=7, columnspan=2)
    home_btn = ttk.Button(frame, text="Return to main menu", width=20,command=lambda: main_window(root))
    home_btn.grid(column=0, row=4, pady=7, columnspan=2)
