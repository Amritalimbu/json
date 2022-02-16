import json
file=open("student.json","r")
a=file.read()
b=json.loads(a)
print(b)