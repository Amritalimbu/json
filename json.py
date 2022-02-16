# import json
# a='{ "country": "india", "religes": "hindu" }'
# json.parse(a)
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x,y)


import json 
# Data to be written 
dictionary ={ 
  "id": "04", 
  "name": "sunil", 
  "department": "HR"
} 
     
# Serializing json  
json_object = json.dumps(dictionary, indent = 4) 
print(json_object)