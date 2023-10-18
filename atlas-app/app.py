import tkinter as tk
from semester_analysis.total_evaluation import total_evaluation_page

def create_popup():
    popup = tk.Toplevel(root)
    popup.geometry('800x500')
    popup.title("Semster Workload Analysis")
    label = tk.Label(popup, text="This is a popup where I will put Semester Workload Analysis.")
    label.pack()

def on_menu_hover(event):
    # Display the dropdown menu when the menu item is hovered
    menu.post(event.x_root, event.y_root)

def on_menu_leave(event):
    # Hide the dropdown menu when the mouse leaves the menu item
    menu.unpost()

root = tk.Tk()
root.title("UMICH Course Analysis")
root.geometry('800x500')

# Create a Menu widget for the top-level items
menu = tk.Menu(root)

# Create a Menu widget for the dropdown
dropdown_menu1 = tk.Menu(menu, tearoff=0)

# Add items to the dropdown menu
dropdown_menu1.add_command(label="Total Evaluation",command=lambda:total_evaluation_page(root))
dropdown_menu1.add_command(label="Workload Evaluation")

# Add top-level items with dropdown menus
menu.add_cascade(label="Semester Analysis", menu=dropdown_menu1)


# Attach the menu to the root window
root.config(menu=menu)

title_label = tk.Label(root, text="Welcome to UMICH Course Analysis", font=("Arial", 16))
title_label.pack(pady=20)

button = tk.Button(root, text="Semester Workload Analysis", command=create_popup)
button.pack()

root.mainloop()