import json
# print(json.dumps(True))
# print(json.dumps(None))
# print(json.dumps("hi"))
# print(json.dumps(90))
# print(json.dumps(93.44))
# print(json.dumps(False))
# print(json.dumps([2,3,4,5]))
# print(json.dumps((3,4,7,8)))



# var = {
#       "Subjects": {
#                   "Maths":85,
#                   "Physics":90
#                    }
#       }
# print()
# out_file = open("myfile.json", "w")
  
# json.dump(dict1, out_file, indent = 6)
  
# out_file.close()
import json
f=open("student_record.txt","wb")
a=[]
while True:
    name=input("enter the name")
    age=int(input("enter the age"))
    city=input("enter the city")
    list=[name,age,city]
    a.append(list)
    choice=input("you want more enter(y/n)?")
    if choice=="n":
        break
json.dump(a,f)
print("record of students")