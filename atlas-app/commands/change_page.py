import tkinter as tk
import json
from components.error_404 import error_404_page
from semester_analysis.total_evaluation import total_evaluation_page
from semester_analysis.workload_evaluation import workload_evaluation_page

def get_final_values(d,term=""):
  final_paths = []
  for key, value in d.items():
    if isinstance(value, dict):
      term+=key+"."
      final_paths.extend(get_final_values(value,term))
    else:
      final_paths.append((term+key,value))
  return final_paths

with open("atlas-app/pages.json", 'r') as json_file:
  paths = json.load(json_file)
path_names = get_final_values(paths)

def change_page(pagename,root):
  for widget in root.winfo_children():
    widget.destroy()
  for path_name,path_value in path_names:
    if path_value==pagename:
      try:
        globals()[path_value.lower().replace(" ", "_")+"_page"](root)
      except:
        error_404_page(root)
