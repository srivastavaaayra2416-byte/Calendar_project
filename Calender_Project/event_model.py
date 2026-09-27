# event_model.py
class Event:
    def __init__(self, date_string, title, description):
        self.date_string = date_string
        self.title = title
        self.description = description

    # Convert object to dictionary for easy saving
    def to_dict(self):
        return {
            "date": self.date_string,
            "title": self.title,
            "description": self.description
        }