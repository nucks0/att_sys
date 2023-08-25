import ctypes
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import Label

import sv_ttk

from attendance import take_attendance
from display import display_attendance
from register import register_student_gui

theme = "dark"
btn_text = "🌞"


def toggle_theme(root, btn):
    global theme, btn_text
    if theme == "dark":
        theme = "light"
        btn_text = "🌜"
        btn["text"] = btn_text
    else:
        theme = "dark"
        btn_text = "🌞"
        btn['text'] = btn_text
    main_window(root)


def title_bar_mode(window, mode):
    # code from https://gist.github.com/Olikonsti/879edbf69b801d8519bf25e804cec0aa
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ctypes.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    if mode == "dark":
        value = 2
    else:
        value = 0
    value = ctypes.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ctypes.byref(value), ctypes.sizeof(value))


def main_window(root):
    clear_window(root)

    frame = ttk.LabelFrame(root, text="Attendance tracker", style='Card.TFrame', padding=(0, 10, 0, 10))
    frame.grid(column=0, row=0)

    button1 = ttk.Button(frame, text="Register", width=20,
                         command=lambda: register_student_gui(root))
    button1.grid(column=0, row=0, padx=20, pady=7)

    button2 = ttk.Button(frame, text="Take Attendance", width=20,
                         command=lambda: take_attendance(root))
    button2.grid(column=0, row=1, padx=20, pady=7)

    button3 = ttk.Button(frame, text="Print Attendance", width=20,
                         command=lambda: display_attendance(root))
    button3.grid(column=0, row=2, padx=20, pady=7)

    button4 = ttk.Button(root, text=btn_text, style='Accent.TButton',
                         command=lambda: toggle_theme(root, button4))
    button4.place(x=0, y=0)

    # dark theme
    sv_ttk.set_theme(theme)
    title_bar_mode(root, theme)


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


class Student:
    def __init__(self, name, cls, sec, rnum, cc):
        self.name = name
        self.cls = int(cls)
        self.sec = sec
        self.rnum = int(rnum)
        self.cc = cc
