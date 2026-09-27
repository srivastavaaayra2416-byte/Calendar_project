# storage_handler.py
import os

FILE_NAME = "events.txt"

def load_events():
    """Reads the text file line by line and organizes events by date."""
    events_dict = {}
    
    # If the file doesn't exist yet, return an empty dictionary
    if not os.path.exists(FILE_NAME):
        return events_dict
    
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip() # Remove invisible newline characters
                if not line:
                    continue
                
                # Split the text line into exactly 3 parts based on the "|" symbol
                parts = line.split("|")
                if len(parts) == 3:
                    date_string = parts[0]
                    title = parts[1]
                    description = parts[2]
                    
                    # Create a list for this date if it doesn't exist yet
                    if date_string not in events_dict:
                        events_dict[date_string] = []
                        
                    # Add the event to that date's list
                    events_dict[date_string].append({"title": title, "description": description})
                    
        return events_dict
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

def save_event(date_string, title, description):
    """Appends a single new line to the text file."""
    
    # Prevent user from typing "|" in their title or description, which would break our format
    safe_title = title.replace("|", "-")
    safe_desc = description.replace("|", "-")
    
    # Open file in "a" (append) mode to just add to the bottom of the file
    with open(FILE_NAME, "a") as file:
        file.write(f"{date_string}|{safe_title}|{safe_desc}\n")