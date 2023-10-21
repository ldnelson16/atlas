import json

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
  try:
    with open("atlasdict"+char+".json","r") as json_file:
      json_info = json.load(json_file)
      
    new_json={}
    for ele in json_info.keys():
      if ele[0]==char:
        new_json[ele]=json_info[ele] 
    
    with open("atlasdict"+char+".json","w") as json_file:
      json.dump(new_json,json_file,indent=1)
  except: 
    pass