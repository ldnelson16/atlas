import tkinter as tk
from semester_analysis.total_evaluation import total_evaluation_page
from components.home_page import home_page
import json

with open("atlas-app/pages.json", 'r') as json_file:
  paths = json.load(json_file)

root = tk.Tk()
root.title("THE ATLAS PROJECT - UMICH Course Analysis")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

home_page(root)

root.mainloop()