# import json
# a='{"amrita":"limbu","age":24}'
# b=json.loads(a)
# print(b)

# import json
# f=open("student_record.txt","wb")
# a=[]
# while True:
#     name=input("enter the name")
#     age=int(input("enter the age"))
#     city=input("enter the city")
#     list=[name,age,city]
#     a.append(list)
#     choice=input("you want more enter(y/n)?")
#     if choice=="n":
#         break
# json.dump(a,f)
# print("record of students")