import tkinter as tk

def error_404_page(root):
    from components.menu import menu
    title_label = tk.Label(root, text="Error 404: Page Not Found", font=("Arial", 16))
    title_label.pack(pady=20)

    menu(root)
