import tkinter as tk
from commands.change_page import change_page
import json

with open("atlas-app/pages.json", 'r') as json_file:
  paths = json.load(json_file)

def on_menu_hover(event, item_name):
    # Display the dropdown menu item when the mouse enters the menu item
    event.widget.itemconfigure(item_name, background='blue')

def on_menu_leave(event, item_name):
    # Reset the background color when the mouse leaves the menu item
    event.widget.itemconfigure(item_name, background='SystemMenu')

def menu(root):
  # Create a Menu widget for the top-level items
  menu = tk.Menu(root)

  for key,value in paths.items():
    if isinstance(value,dict):
      # Create a Menu widget for the dropdown
      dropdown_menu = tk.Menu(menu, tearoff=0)
      # Add items to the dropdown menu
      for item,val in value.items():
        dropdown_menu.add_command(label=val,command=lambda:change_page(val,root))
      # Add top-level items with dropdown menus
      menu.add_cascade(label=key.replace("_"," ").title(), menu=dropdown_menu)

  # Attach the menu to the root window
  root.config(menu=menu)

