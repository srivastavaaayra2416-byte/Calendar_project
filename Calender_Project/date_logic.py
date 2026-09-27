# date_logic.py
import calendar
import datetime

def get_current_month_year():
    """Returns the current month and year."""
    now = datetime.datetime.now()
    return now.month, now.year

def get_month_calendar(year, month):
    """
    Returns a matrix representing a month's calendar.
    Days outside the month are represented by 0.
    """
    cal = calendar.TextCalendar(calendar.SUNDAY)
    return cal.monthdayscalendar(year, month)

def get_month_name(month_number):
    """Converts month number (1-12) to Name (January-December)"""
    return calendar.month_name[month_number]