# main.py
import tkinter as tk
from ui_components import CalendarApp

if __name__ == "__main__":
    # Create the main window and pass it to the App
    root = tk.Tk()
    app = CalendarApp(root)
    
    # Run the application loop
    root.mainloop()
    