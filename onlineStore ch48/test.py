# name = "Richard"
# last_name = "Dillard"
# age = "32"
# found = False
# print(name)


# if age < 100:
#     print(" great youre not that old")
#     print("im inside of the statement")
# elif age >100:
#     print(" yeah seems that youre not the young anymore")
# else:
#     print("i dont know how you got here")
# print("im outside of the if stamtment")



# def sayHello():
#     print("hello there")
    
# sayHello()

# colors =["black", "blue", "green",]
# colors.append("pink")

# print(colors[0])

# print(colors)


# for x in colors:
#     print(x)
    
# print(colors)


# me = {
#     "firstName": "Richard",
#     "lastName": "Dillard",
#     "age": 32
# }
# print(me)

# me["age"]=99
# print(me)

def printMenu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    
printMenu()
opt = input("select the option")

number1=float(input("please give me the first number"))
number2=float(input("please give me the second number"))

if opt == "1":
    total= number1 + number2
    print("the total is:"+ str(total))