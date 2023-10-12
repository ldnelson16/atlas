import json

# read in ideal results as results
file_path = "webscraper/data/atlasdictfinal.json"
with open(file_path, 'r') as json_file:
  results = json.load(json_file)

lettersgotten = {}
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
  lettersgotten[letter]={"Gotten":0,"Missed":0}
  try:
    file_path = "webscraper/data/letters/atlasdict"+letter+".json"
    with open(file_path, 'r') as json_file:
      letterresults = json.load(json_file)
    for key in results:
      if key[0]==letter:
        results[key]=letterresults[key]
  except: 
    pass
titles_gotten = titles_missed = 0
for key in results:
  if results[key]["Class Title"]!=None:
    titles_gotten+=1
    lettersgotten[key[0]]["Gotten"]+=1
  else:
    titles_missed+=1
    lettersgotten[key[0]]["Missed"]+=1
  

print(json.dumps(lettersgotten,indent=1))
sumgot=0
summissed=0
for key in lettersgotten:
  sumgot+=lettersgotten[key]["Gotten"]
  summissed+=lettersgotten[key]["Missed"]
print("Got:",sumgot,", Missed:",summissed)

file_path = "webscraper/data/atlasdictfinal.json"
with open(file_path, 'w') as json_file:
    json.dump(results, json_file,indent=2)

