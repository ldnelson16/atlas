import tkinter as tk
import tkinter.ttk as ttk
from ttkwidgets.autocomplete import AutocompleteEntry
import json
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_directory, "../../webscraper/data/atlasdictfinal.json")
with open(json_file_path,"rb") as json_file:
    classdict = json.load(json_file)
    classnames = classdict.keys()

def get_entries(root,entries,submit_button,right_frame):
    submit_button.config(bg="darkgrey")
    root.after(200, submit_button.config(bg="grey"))
    results = []
    for entry in entries:
        if (entry.get()!=""):
            results.append(entry.get())

    # Create a ttk.Treeview widget as a table
    table = ttk.Treeview(right_frame, columns=("Class", "Workload"), show="headings")
    table.heading("Class", text="Class")
    table.heading("Workload", text="Workload")

    data = [(result,classdict[result]["Workload"]) if classdict[result]["Workload"]!=None else "-" for result in results]
    for item in data:
        table.insert("", "end", values=item)
    table.pack(pady=20)

    table_stats = ttk.Treeview(right_frame,columns=("Stat","Value"),show="headings")
    table_stats.heading("Stat", text="Stat")
    table_stats.heading("Value", text="Value")

    classes_w_data = sum([1 if classdict[result]["Workload"]!=None else 0 for result in results])
    total_credits = sum([classdict[result]["Credits"] if classdict[result]["Workload"]!=None else 0 for result in results])
    total_workload = sum([classdict[result]["Workload"] if classdict[result]["Workload"]!=None else 0 for result in results])
    avg_credits = total_credits / classes_w_data
    stats = [
            ("Classes w/ Data",classes_w_data),
            ("Average Class Workload", "{:.2f}".format(total_workload/classes_w_data)),
            ("Average Weighted Class Workload","{:.2f}".format(sum([classdict[result]["Workload"]*classdict[result]["Credits"]/avg_credits if classdict[result]["Workload"]!=None else 0 for result in results])/classes_w_data)),
            ("Total Workload",total_workload)
            ]
    for item in stats:
        table_stats.insert("","end",values=item)
    table_stats.pack(pady=20)

def workload_evaluation_page(root):
    title_label = tk.Label(root, text="Workload Evaluation Page", font=("Arial", 16))
    title_label.pack(pady=20, fill="x")

    separator = ttk.Separator(root, orient='horizontal')
    separator.pack(fill="x", padx=5)

    from components.menu import menu
    menu(root)

    left_frame = tk.Frame(root)
    left_frame.pack(side="left", fill="both", expand=True)

    input_label = tk.Label(left_frame, text="Input Your Classes for This Semster", font=("Arial",14))
    input_label.pack(pady=20)

    input_separator = ttk.Separator(left_frame,orient='horizontal')
    input_separator.pack(fill="x",padx=55,pady=5)

    entries= []
    for i in range(10):
        entry = AutocompleteEntry( 
            left_frame,
            width=30, 
            font=('Arial', 14),
            completevalues=classnames
            )
        entry.pack(pady=5,padx=55)
        entries.append(entry)

    submit_button = tk.Button(left_frame, text="Submit", bg="grey", command=lambda: get_entries(root,entries,submit_button,right_frame))
    submit_button.pack()

    style = ttk.Style()
    style.configure("Separator.TSeparator", background="lightgray")

    separator = ttk.Separator(root, orient='vertical', style="Separator.TSeparator")
    separator.pack(side="left", fill="y", padx=5)

    right_frame = tk.Frame(root)
    right_frame.pack(side="left", fill="both", expand=True)

