f=open("amrita.txt","w")
f.write("morning","evening","finding","monday")
i=0
a=[]
while i<=len(f):
    if f[i]=="ing":
        a.append([i])
    i=i+1
print(a)