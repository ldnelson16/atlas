import tkinter as tk
import tkinter.ttk as ttk
from ttkwidgets.autocomplete import AutocompleteEntry
from data.atlasdict_json import atlasdict

classnames = atlasdict.keys()

def get_entries(root,entries,submit_button,right_frame):
    submit_button.config(bg="darkgrey")
    root.after(200, submit_button.config(bg="grey"))
    results = []
    for entry in entries:
        if (entry.get()!=""):
            results.append(entry.get())

    for widget in right_frame.winfo_children():
        widget.destroy()

    table_stats = ttk.Treeview(right_frame,columns=("Class/Stat","Desire to Take","Understanding","Workload","Expectations","Increased Interest"),show="headings")
    table_stats.heading("Class/Stat", text="Class/Stat")
    table_stats.heading("Desire to Take", text="Desire to Take")
    table_stats.heading("Understanding", text="Understanding")
    table_stats.heading("Workload", text="Workload")
    table_stats.heading("Expectations", text="Expectations")
    table_stats.heading("Increased Interest", text="Increased Interest")

    info = [(result,atlasdict[result]["Desire to Take"],atlasdict[result]["Understanding"],atlasdict[result]["Workload"],atlasdict[result]["Expectations"],atlasdict[result]["Increased Interest"]) if atlasdict[result]["Workload"]!=None else (result,"-","-","-","-","-") for result in results]

    classes_w_data = sum([1 if atlasdict[result]["Workload"]!=None else 0 for result in results])
    total_credits = sum([atlasdict[result]["Credits"] if atlasdict[result]["Credits"]!=None else 0 for result in results])
    avg_credits = total_credits / classes_w_data
    total_dtt = sum([atlasdict[result]["Desire to Take"] if atlasdict[result]["Desire to Take"]!=None else 0 for result in results])
    weighted_dtt = sum([atlasdict[result]["Desire to Take"]*atlasdict[result]["Credits"]/avg_credits if atlasdict[result]["Desire to Take"]!=None else 0 for result in results])/classes_w_data
    total_understanding = sum([atlasdict[result]["Understanding"] if atlasdict[result]["Understanding"]!=None else 0 for result in results])
    weighted_understanding = sum([atlasdict[result]["Understanding"]*atlasdict[result]["Credits"]/avg_credits if atlasdict[result]["Understanding"]!=None else 0 for result in results])/classes_w_data
    total_workload = sum([atlasdict[result]["Workload"] if atlasdict[result]["Workload"]!=None else 0 for result in results])
    weighted_workload = sum([atlasdict[result]["Workload"]*atlasdict[result]["Credits"]/avg_credits if atlasdict[result]["Workload"]!=None else 0 for result in results])/classes_w_data
    total_expectations = sum([atlasdict[result]["Expectations"] if atlasdict[result]["Expectations"]!=None else 0 for result in results])
    weighted_expectations = sum([atlasdict[result]["Expectations"]*atlasdict[result]["Credits"]/avg_credits if atlasdict[result]["Expectations"]!=None else 0 for result in results])/classes_w_data
    total_ii = sum([atlasdict[result]["Increased Interest"] if atlasdict[result]["Increased Interest"]!=None else 0 for result in results])
    weighted_ii = sum([atlasdict[result]["Increased Interest"]*atlasdict[result]["Credits"]/avg_credits if atlasdict[result]["Increased Interest"]!=None else 0 for result in results])/classes_w_data

    info.append(("","","","","",""))
    info.append(("Classes w/ Data",str(classes_w_data)+"/"+str(len(results)),"","","",""))
    info.append(("Average","{:.2f}".format(total_dtt/classes_w_data),"{:.2f}".format(total_understanding/classes_w_data),"{:.2f}".format(total_workload/classes_w_data),"{:.2f}".format(total_expectations/classes_w_data),"{:.2f}".format(total_ii/classes_w_data)))
    info.append(("Weighted Average","{:.2f}".format(weighted_dtt),"{:.2f}".format(weighted_understanding),"{:.2f}".format(weighted_workload),"{:.2f}".format(weighted_expectations),"{:.2f}".format(weighted_ii)))
    info.append(("Total",total_dtt,total_understanding,total_workload,total_expectations,total_ii))
    statuses = []
    for wtd in [weighted_dtt,weighted_understanding,weighted_workload,weighted_expectations,weighted_ii]:
        composite = wtd*total_credits
        statuses.append(composite)
    info.append(("Status",statuses[0],statuses[1],statuses[2],statuses[3],statuses[4]))

    for item in info:
        table_stats.insert("","end",values=item)
    table_stats.pack(pady=20)

def total_evaluation_page(root):
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

