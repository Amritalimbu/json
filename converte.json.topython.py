# json to python
import json
j='{"name":"sita","age":25,"city":"bangalore"}'
p=json.loads(j)
print(p)
# print(json.loads(j,separators=("@","$")))



# python to json
import json
j='{"name":"sita","age":25,"city":"bangalore"}'
p=json.loads(j)
print(p)
# print(json.loads(j,separators=("@","$")))
# print(j)
# print(json.dumps(p,separators=("@","$")))