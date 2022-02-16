import pickle
def write():
    f=open("student.dat","wb")
    record=[]
    while True:
        name=input("enter the name")
        age=int(input("enter the age"))
        marks=int(input("enter the marks"))
        list=[name,age,marks]
        record.append(list)
        choice=input("more record(y/n)?")
        if choice=="n":
            break
    pickle.dump(record,f)
    print("date stored sucessfully")
write()

def read():
    f=open("student.dat","rb")
    r=pickle.load(f)
    # print(r)
    for i in r:
        print(i)
read()

