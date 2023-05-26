# req_age=4
# h_age=5

# if req_age==h_age:
#     print("Age is equal")
# elif h_age>req_age: 
#     print("Hammad can go to school")
# else:
#     print("Hammad can not go to school")


class_attended=input("Enter number of classes you attended : ")
total_classes=48
class_attended=int(class_attended)
per=float(class_attended/total_classes)
per*=100

if per>=75:
    print("Percentage : ",per)
    print("You are eligible for exam")
else:
    print("Percentage : ",per)
    print("You are not eligible for exam")

