import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from entry import *
from button import *
from utils import *

class cls_frame_DateSelector_view(tk.Frame):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.frames = self.create_frames()
        self.create_widgets()

    def create_frames(self):
        frames = []
        for i in range(2):
            frame_name = f"frame_row_{i+1}"
            frame = ttk.Frame(self, padding="3", borderwidth=0, relief="flat", name=frame_name)
            frame.grid(row=i, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
            frames.append(frame)
        frames[0].columnconfigure(0, weight=1)
        frames[0].columnconfigure(1, weight=1)
        frames[0].columnconfigure(2, weight=1)
        frames[1].columnconfigure(0, weight=1)
        frames[1].columnconfigure(1, weight=1)
        frames[1].columnconfigure(2, weight=1)
        frames[1].columnconfigure(3, weight=1)
        frames[1].columnconfigure(4, weight=1)
        frames[1].columnconfigure(5, weight=1)
        return frames

    def create_widgets(self):
        self.label = ttk.Label(self.frames[0], text="Chọn ngày:")
        self.label.grid(row=0, column=0, padx=(2, 2), pady=0)

        # Entry 1 (from this date)
        self.entry_01 = cls_my_date_time_entry_num_01(self.frames[0], width=20, name="start_date_entry")
        self.entry_01.insert(0, self.first_day_of_month())
        self.entry_01.grid(row=0, column=1, padx=(0, 2), pady=0, sticky="ew")

        # Entry 2 (to this date)
        self.entry_02 = cls_my_date_time_entry_num_01(self.frames[0], width=20, name="end_date_entry")
        self.entry_02.insert(0, self.today_date())
        self.entry_02.grid(row=0, column=2, padx=(0, 0), pady=0, sticky="ew")

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        # Button (This week)
        clear_button = cls_my_button_num_02(self.frames[0], text="Clear", command=lambda: self.clear_entries(*self.clear_all()))
        clear_button.grid(row=0, column=3, padx=2, pady=0)
        
        # Button (This week)
        this_week_button = cls_my_button_num_02(self.frames[1], text="This week", command=lambda: self.clear_entries(*self.this_week()))
        this_week_button.grid(row=0, column=0, padx=2, pady=0)

        # Button (Last week)
        last_week_button = cls_my_button_num_02(self.frames[1], text="Last week", command=lambda: self.clear_entries(*self.last_week()))
        last_week_button.grid(row=0, column=1, padx=2, pady=0)

        # Button (This month)
        this_month_button = cls_my_button_num_02(self.frames[1], text="This month", command=lambda: self.clear_entries(*self.this_month()))
        this_month_button.grid(row=0, column=2, padx=2, pady=0)

        # Button (Last month)
        last_month_button = cls_my_button_num_02(self.frames[1], text="Last month", command=lambda: self.clear_entries(*self.last_month()))
        last_month_button.grid(row=0, column=3, padx=2, pady=0)

        # Button (This year)
        this_year_button = cls_my_button_num_02(self.frames[1], text="This year", command=lambda: self.clear_entries(*self.this_year()))
        this_year_button.grid(row=0, column=4, padx=2, pady=0)

        # Button (Last year)
        last_year_button = cls_my_button_num_02(self.frames[1], text="Last year", command=lambda: self.clear_entries(*self.last_year()))
        last_year_button.grid(row=0, column=5, padx=2, pady=0)

    # Function to clear the entries
    def clear_entries(self, start_date, end_date):
        self.entry_01.delete(0, tk.END)
        self.entry_02.delete(0, tk.END)
        self.entry_01.insert(0, start_date)
        self.entry_02.insert(0, end_date)

    # Function to get the first day of the current month
    def first_day_of_month(self):
        today = datetime.today()
        return today.replace(day=1).strftime('%d-%m-%Y')

    # Function to get today's date
    def today_date(self):
        return datetime.today().strftime('%d-%m-%Y')

    # Function to get the start and end date for the current week
    def clear_all(self):
        return '', ''
    
    # Function to get the start and end date for the current week
    def this_week(self):
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())  # Monday
        end_of_week = start_of_week + timedelta(days=6)  # Sunday
        return start_of_week.strftime('%d-%m-%Y'), end_of_week.strftime('%d-%m-%Y')

    # Function to get the start and end date for the last week
    def last_week(self):
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday()) - timedelta(weeks=1)  # Last week's Monday
        end_of_week = start_of_week + timedelta(days=6)  # Last week's Sunday
        return start_of_week.strftime('%d-%m-%Y'), end_of_week.strftime('%d-%m-%Y')

    # Function to get the start and end date for the current month
    def this_month(self):
        today = datetime.today()
        start_of_month = today.replace(day=1)  # First day of this month
        next_month = today.replace(day=28) + timedelta(days=4)  # Go to next month
        end_of_month = next_month - timedelta(days=next_month.day)  # Last day of this month
        return start_of_month.strftime('%d-%m-%Y'), end_of_month.strftime('%d-%m-%Y')

    # Function to get the start and end date for the last month
    def last_month(self):
        today = datetime.today()
        first_day_of_last_month = today.replace(day=1) - timedelta(days=1)
        start_of_last_month = first_day_of_last_month.replace(day=1)  # First day of last month
        end_of_last_month = first_day_of_last_month  # Last day of last month
        return start_of_last_month.strftime('%d-%m-%Y'), end_of_last_month.strftime('%d-%m-%Y')

    # Function to get the start and end date for the current year
    def this_year(self):
        today = datetime.today()
        start_of_year = today.replace(month=1, day=1)  # First day of this year
        end_of_year = today.replace(month=12, day=31)  # Last day of this year
        return start_of_year.strftime('%d-%m-%Y'), end_of_year.strftime('%d-%m-%Y')

    # Function to get the start and end date for the last year
    def last_year(self):
        today = datetime.today()
        start_of_last_year = today.replace(year=today.year-1, month=1, day=1)  # First day of last year
        end_of_last_year = today.replace(year=today.year-1, month=12, day=31)  # Last day of last year
        return start_of_last_year.strftime('%d-%m-%Y'), end_of_last_year.strftime('%d-%m-%Y')
