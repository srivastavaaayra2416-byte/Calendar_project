# GUI Calendar & Event Manager

## Overview
A desktop calendar application built with Python and Tkinter. It allows users to navigate through months and years, and click on any specific date to add, view, or manage personal events/to-do lists.

## Features
* Interactive monthly grid view
* Add events with titles and descriptions to specific days
* Persistent local storage (saves events to a JSON file)
* Month/Year navigation

## Technologies/Tools Used
* Python 3.x
* Tkinter (GUI framework)
* .txt

## Steps to Install & Run
1. Ensure Python 3 is installed on your system.
2. Clone this repository.
3. Open a terminal/command prompt in the project folder.
4. Run the command: `python main.py`

## Instructions for testing
1. Run the application.
2. Click on today's date on the grid.
3. Type a title ("Submit Project") and a description, then click Save.
4. Close the application entirely, then run `python main.py` again.
5. Click on the same date—your saved event will still be there, proving data persistence.
