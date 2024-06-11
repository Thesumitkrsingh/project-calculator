print("simple calculator")
print(1,"adittion")
print(2,"substraction")
print(3,"multiplication")
choice=input("enter your choice(1,2,3):")
num1=int(input("enter your number"))
num2=int(input("enter your second number"))
if choice == '1':
    result=num1+num2
elif choice == '2':
    result=num1-num2
elif choice == '3':
    result=num1*num2
else:
    result=print("invalid choice please chosse valid number (1,2,3)")
print("Result",result)       
