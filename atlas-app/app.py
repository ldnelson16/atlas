import tkinter as tk
from semester_analysis.total_evaluation import total_evaluation_page
from components.menu import menu
import json

with open("atlas-app/pages.json", 'r') as json_file:
  paths = json.load(json_file)

root = tk.Tk()
root.title("UMICH Course Analysis")
root.geometry('800x500')

# Create a Menu widget for the top-level items
menu(root)

title_label = tk.Label(root, text="Welcome to UMICH Course Analysis", font=("Arial", 16))
title_label.pack(pady=20)

root.mainloop()