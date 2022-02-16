import json
file="textfile.json"
dict={}
with open (file) as fn:
    for d in fn:
        key,desc=d.strip().split(None,1)
        dict[key]=desc.strip()
otfile=open("textfile.json","w")
json.dump(dict,otfile)
otfile.close()