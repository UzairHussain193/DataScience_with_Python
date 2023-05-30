def printname():
    print("My name is Uzair Hussain")
    print("I am 20 years old")
    print("I am a student of Computer Science")
    
# printname()

def exam_eligibility():
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


# print("\n\nChecking your exam eligibility: ")
# exam_eligibility()

def text(var):
    print("Hello ",var)
# text("Uzair")

def school_calculator():
    age=input("enter your age: ")
    age=int(age)

    if age<5:
        print("You are not eligible for school")
    elif age==5:
        print("You are eligible for school")
    elif age>5:
        print("You are eligible for higher school")

# school_calculator()


def futureage(age):
    newage=age+20
    return newage

fage=futureage(17)
print(fage) 

