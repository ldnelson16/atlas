import tkinter as tk
from commands.change_page import change_page

def on_menu_hover(event, item_name):
    # Display the dropdown menu item when the mouse enters the menu item
    event.widget.itemconfigure(item_name, background='blue')

def on_menu_leave(event, item_name):
    # Reset the background color when the mouse leaves the menu item
    event.widget.itemconfigure(item_name, background='SystemMenu')

def menu(root):
  # Create a Menu widget for the top-level items
  menu = tk.Menu(root)

  # Create a Menu widget for the dropdown
  dropdown_menu1 = tk.Menu(menu, tearoff=0)

  # Add items to the dropdown menu
  dropdown_menu1.add_command(label="Total Evaluation",command=lambda:change_page("Total Evaluation",root))
  dropdown_menu1.add_command(label="Workload Evaluation",command=lambda:change_page("Workload Evaluation",root))

  # Add top-level items with dropdown menus
  menu.add_cascade(label="Semester Analysis", menu=dropdown_menu1)

  # Attach the menu to the root window
  root.config(menu=menu)

