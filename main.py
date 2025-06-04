def lovecode ():
  print("i see that you picked option 1! hello! I love you so much!")
  mylovesname = input("please enter your name:")
  if mylovesname == "Tommy" or mylovesname == "tommy russoniello" or mylovesname == "Tommy russoniello" or mylovesname == "tommy Russoniello" or mylovesname == "tommy" or mylovesname == "Tommy Russoniello":
    print("I LOVE YOU!!!!")
  else: 
    print("get out of here! I want Tommy")
#if you're reading this, you're in the mainframe😎

def calculator ():
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, * or /): ")

        if operator == "+":
            print("Result:", number1 + number2)
        elif operator == "-":
            print("Result:", number1 - number2)
        elif operator == "*":
            print("Result:", number1 * number2)
        elif operator == "/":
            if number2 != 0:
                print("Result:", number1 / number2)
            else:
                print("HAH you thought i wouldn't remember to make this work! you can't divide by zero")
        else: 
            print("plz contact tech support at 267-***-****")



print("hello! welcome to the Tommy Code!! You have two options:")
print("1. Love Code")
print("2. Calculator")

choice = input("Enter 1 or 2: ")

if choice == "1":
    lovecode()
elif choice == "2":
    calculator()
else:
    print("do you even know how to type??? I said 1 or 2")
