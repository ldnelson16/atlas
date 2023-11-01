import json

with open("webscraper/data/atlasdictfinal1.json","r") as file:
  results = json.load(file)

to_remove = []
for key in results:
  if results[key]["Median Grade"] == "N/A":
    results[key]["Median Grade"] = None
  elif results[key]["Median Grade"]!=None and "~" in results[key]["Median Grade"]:
    results[key]["Median Grade"] = results[key]["Median Grade"].split("~")
  elif results[key]["Median Grade"]!=None:
    results[key]["Median Grade"] = [results[key]["Median Grade"],results[key]["Median Grade"]]
  if results[key]["Class Title"]==None:
    to_remove+=[key]
  try: 
    x=float(results[key]["Credits"])
    results[key]["Credits"] = [float(results[key]["Credits"]),float(results[key]["Credits"])]
  except:
    try:
      results[key]["Credits"] = [float(x) for x in results[key]["Credits"].split('-')]
    except:
      pass

for key in to_remove:
  del results[key]

with open("webscraper/data/atlasdictfinal2.json","w") as file:
  json.dump(results,file,indent=1)
  