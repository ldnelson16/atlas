import json

with open("webscraper/data/atlasdictfinal1.json","r") as file:
  results = json.load(file)

to_remove = []
for key in results:
  if results[key]["Class Title"]==None:
    print(key,"missing")
    to_remove+=[key]
  try: 
    x=float(results[key]["Credits"])
    # print(key,[float(results[key]["Credits"]),float(results[key]["Credits"])])
    results[key]["Credits"] = [float(results[key]["Credits"]),float(results[key]["Credits"])]
  except:
    try:
      # print(key,[float(x) for x in results[key]["Credits"].split('-')])
      results[key]["Credits"] = [float(x) for x in results[key]["Credits"].split('-')]
    except:
      # print(key,results[key]["Credits"])
      pass

for key in to_remove:
  del results[key]

with open("webscraper/data/atlasdictfinal2.json","w") as file:
  json.dump(results,file,indent=1)
  