import json
a={"apple":"red"
   ,"mango":"yellow",
   "vegetable":"green"
   }
print(a)
b=json.dumps(a)
print(b)
print(type(b))