import tkinter.messagebox
from tkinter import ttk

import mysql.connector


def create_db(db_name):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="attendancesys"
    )

    cursor = db.cursor()

    # Check if database exists, if it doesn't then create one
    cursor.execute("SHOW DATABASES")

    flag = False
    for x in cursor:
        if db_name in x:
            flag = True

    if not flag:
        cursor.execute(f"CREATE DATABASE {db_name}")
        print("Database created")

    # select newly created db
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="attendancesys",
        database=db_name
    )


def create_table(cursor, table_name):
    # Check if tables, rows and columns exist, if they don't then create them
    flag = False
    cursor.execute("SHOW TABLES")
    for x in cursor:
        if table_name in x:
            flag = True

    if not flag:
        cursor.execute(
            f"CREATE TABLE `{table_name}` (name VARCHAR(255), cls INT, sec VARCHAR(255), rnum INT, cc VARCHAR(255))"
        )
        print("Table created")


def print_table(popup, frames, table_name):

    mydb = Database()
    result = mydb.get_all_table_elem(popup, table_name)

    if result is not None:
        row = 1
        column = 0

        for student in result:
            for detail in student:
                lbl = ttk.Label(frames[column], text=detail)
                lbl.grid(column=column, row=row)
                column += 1
            print()
            row += 1
            column = 0


class Database:
    def __init__(self):
        self.db = create_db('attendance_sys')
        self.cursor = self.db.cursor()

    def add_entry(self, student, table_name):
        create_table(self.cursor, table_name)
        sql = f"INSERT INTO `{table_name}` (name, cls, sec, rnum, cc) VALUES (%s, %s, %s, %s, %s)"
        val = (student.name, student.cls, student.sec, student.rnum, student.cc)
        self.cursor.execute(sql, val)
        self.db.commit()
        print(self.cursor.rowcount, "Record inserted")

    def manual_fetch_student(self, cls, sec, rnum):
        from utils import Student

        sql = f"SELECT * FROM students WHERE cls = {cls} AND sec = '{sec}' AND rnum = {rnum}"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()

        if result is None:
            tkinter.messagebox.showerror(
                title="Invalid details",
                message=f"Student does not exist\nRecheck details or register new student"
            )
            print(f"Invalid details entered: (cls: {cls}, sec = {sec}, rnum = {rnum})")
        else:
            s = Student(result[0], result[1], result[2], result[3], result[4])
            return s

    def cc_fetch_student(self, cc):
        from utils import Student

        sql = f"SELECT * FROM students WHERE cc = '{cc}'"
        self.cursor.execute(sql)

        try:
            result = self.cursor.fetchall()[0]  # fetchone is failing when more than one same entry
        except IndexError:
            result = None

        if result is None:
            tkinter.messagebox.showerror(
                title="Invalid computer code",
                message=f"Computer code does not exist\nRecheck cc or register new student"
            )
            print(f"Invalid cc entered: {cc}")
        else:
            s = Student(result[0], result[1], result[2], result[3], result[4])
            return s

    def get_all_table_elem(self, popup, table_name):
        try:
            self.cursor.execute(f"SELECT * FROM `{table_name}`")
            return self.cursor.fetchall()
        except:
            popup.destroy()
            tkinter.messagebox.showerror(
                title="Not found",
                message=f"Either the date is invalid OR no record exists for that date"
            )
            print(f"Invalid date entered")

    def delete(self):
        self.cursor.execute("DROP DATABASE attendance_sys")
        print("Database deleted")
