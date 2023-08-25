from db import Database
import tkinter as tk
from tkinter import ttk

name = ""
cls = ""
sec = ""
rnum = ""
cc = ""


def db_add():
    from utils import Student
    global name, cls, sec, rnum, cc
    s = Student(name, int(cls), sec, int(rnum), cc)

    mydb = Database()
    mydb.add_entry(s, 'students')

    print("Student registered!")
    print(f"Name: {s.name}")
    print(f"Class: {s.cls}, Sec: {s.sec}")
    print(f"Roll No: {s.rnum}")
    print(f"CC: {s.cc}")


def generate_cc():
    global name, cls, sec, rnum, cc
    cc = f"{name[0]}-{cls}-{sec}-{rnum}"
    print(f"CC generated: {cc}")


def details(txt1, txt2, txt3, txt4):
    global name, cls, sec, rnum, cc
    name = txt1.get()
    cls = txt2.get()
    sec = txt3.get()
    rnum = txt4.get()
    generate_cc()

    db_add()

    # Clean the text fields
    txt1.delete(0, tk.END)
    txt2.delete(0, tk.END)
    txt3.delete(0, tk.END)
    txt4.delete(0, tk.END)

    tk.messagebox.showinfo(
        title="Success!",
        message=f"Student Registered.\nComputer code = {cc}"
    )


def register_student_gui(root):
    from utils import clear_window, main_window
    clear_window(root)

    frame = ttk.LabelFrame(root, text="Mark attendance", style='Card.TFrame', padding=(20, 20, 20, 20))
    frame.grid(column=0, row=0)

    lbl2 = ttk.Label(frame, text="Name: ")
    lbl2.grid(column=0, row=1, padx=6, pady=7)
    txt1 = ttk.Entry(frame, width=15)
    txt1.grid(column=1, row=1, padx=7, pady=7)

    lbl3 = ttk.Label(frame, text="Class: ")
    lbl3.grid(column=0, row=2, padx=6, pady=7)
    txt2 = ttk.Entry(frame, width=15)
    txt2.grid(column=1, row=2, padx=7, pady=7)

    lbl4 = ttk.Label(frame, text="Sec: ")
    lbl4.grid(column=0, row=3, padx=6, pady=7)
    txt3 = ttk.Entry(frame, width=15)
    txt3.grid(column=1, row=3, padx=7, pady=7)

    lbl5 = ttk.Label(frame, text="Roll No: ")
    lbl5.grid(column=0, row=4, padx=6, pady=7)
    txt4 = ttk.Entry(frame, width=15)
    txt4.grid(column=1, row=4, padx=7, pady=7)

    submit_btn = ttk.Button(frame, text="Submit", width=20, style='Accent.TButton',
                            command=lambda: details(txt1, txt2, txt3, txt4))
    submit_btn.grid(column=0, row=5, columnspan=2, pady=7)
    home_btn = ttk.Button(frame, text="Return to main menu", width=20, command=lambda: main_window(root))
    home_btn.grid(column=0, row=6, columnspan=2, pady=7)
