

x=1
y=4
x=int(x)
y=int(y)
# print("Table of ",y," using while loop")
# while(x<=10):
#     print(y," * ",x," = ",(x*y))
#     x+=1

# print("Table of ",y," using for loop")
# for x in range(1,10):
#     print(y," * ",x," = ",(x*y))
#     x+=1


days=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]

for d in days:
    if d=="Wed":
        continue
    if d=="F ri":
        break
    print(d)

