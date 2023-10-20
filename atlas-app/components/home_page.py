import tkinter as tk

def home_page(root):
  for widget in root.winfo_children():
    widget.destroy()

  title_label = tk.Label(root, text="Welcome to UMICH Course Analysis", font=("Arial", 16))
  title_label.pack(pady=20)

  from components.menu import menu
  menu(root)