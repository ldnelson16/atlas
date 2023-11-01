import json

new_json={}
totalfullmissed=0
totalmissed=0
totalhit=0
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
  try:
    with open("webscraper/data/letters/atlasdict"+char+".json","r") as json_file:
      json_info = json.load(json_file)

    fullmissed=0
    missed=0
    hit=0
    for key in json_info:
      new_json[key]=json_info[key]
      if (json_info[key]["Class Title"]==None):
        fullmissed+=1
      elif (json_info[key]["Desire to Take"]==None or json_info[key]["Understanding"]==None or json_info[key]["Workload"]==None or json_info[key]["Expectations"]==None or json_info[key]["Increased Interest"]==None):
        missed+=1
      else:
        hit+=1

    print(char,"(hit, missed, fullmissed) = ("+str(hit)+","+str(missed)+","+str(fullmissed)+")")
    totalfullmissed+=fullmissed
    totalmissed+=missed
    totalhit+=hit

    new_json.extend(json_info)

  except: 
    pass
with open("atlasdictfinal.json","w") as json_file:
  json.dump(new_json,json_file,indent=1)

print("(hit, missed, fullmissed) = ("+str(totalhit)+","+str(totalmissed)+","+str(totalfullmissed)+")")