# ui_components.py
import tkinter as tk
from tkinter import messagebox
import date_logic
import storage_handler

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calendar & Event Manager")
        self.root.geometry("600x500")
        
        # Get current date
        self.current_month, self.current_year = date_logic.get_current_month_year()
        
        self.setup_ui()

    def setup_ui(self):
        # Clear existing widgets if any (used for refreshing)
        for widget in self.root.winfo_children():
            widget.destroy()

        # Header Frame (Month/Year and Buttons)
        header_frame = tk.Frame(self.root)
        header_frame.pack(pady=10)

        prev_btn = tk.Button(header_frame, text="< Prev", command=self.prev_month)
        prev_btn.grid(row=0, column=0, padx=10)

        month_label_text = f"{date_logic.get_month_name(self.current_month)} {self.current_year}"
        month_label = tk.Label(header_frame, text=month_label_text, font=("Arial", 16, "bold"))
        month_label.grid(row=0, column=1, padx=20)

        next_btn = tk.Button(header_frame, text="Next >", command=self.next_month)
        next_btn.grid(row=0, column=2, padx=10)

        # Days of week header
        days_frame = tk.Frame(self.root)
        days_frame.pack()
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(days):
            tk.Label(days_frame, text=day, width=8, font=("Arial", 10, "bold")).grid(row=0, column=i)

        # Calendar Grid
        grid_frame = tk.Frame(self.root)
        grid_frame.pack(pady=10)

        month_days = date_logic.get_month_calendar(self.current_year, self.current_month)
        
        for row_idx, week in enumerate(month_days):
            for col_idx, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(grid_frame, text=str(day), width=6, height=3, 
                                    command=lambda d=day: self.open_event_window(d))
                    btn.grid(row=row_idx, column=col_idx, padx=2, pady=2)

    def prev_month(self):
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.setup_ui()

    def next_month(self):
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.setup_ui()

    def open_event_window(self, day):
        # Create a popup window
        top = tk.Toplevel(self.root)
        selected_date = f"{self.current_year}-{self.current_month:02d}-{day:02d}"
        top.title(f"Events for {selected_date}")
        top.geometry("300x400")

        tk.Label(top, text="Add New Event:", font=("Arial", 12, "bold")).pack(pady=5)
        
        tk.Label(top, text="Title:").pack()
        title_entry = tk.Entry(top, width=30)
        title_entry.pack()

        tk.Label(top, text="Description:").pack()
        desc_entry = tk.Entry(top, width=30)
        desc_entry.pack()

        def save_btn_clicked():
            t = title_entry.get()
            d = desc_entry.get()
            if t == "":
                messagebox.showerror("Error", "Title cannot be empty!")
                return
            storage_handler.save_event(selected_date, t, d)
            messagebox.showinfo("Success", "Event Saved!")
            top.destroy()

        tk.Button(top, text="Save Event", command=save_btn_clicked).pack(pady=10)

        # Display Existing Events
        tk.Label(top, text="Existing Events:", font=("Arial", 12, "bold")).pack(pady=10)
        events = storage_handler.load_events()
        
        if selected_date in events:
            for ev in events[selected_date]:
                tk.Label(top, text=f"• {ev['title']} - {ev['description']}").pack()
        else:
            tk.Label(top, text="No events for this day.").pack()