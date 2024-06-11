#SIMPLE CALCULATOR#

num1=int(input("Enter the first value: "))
num2=int(input("Enter the second value: "))


print('''
+ ADD
- SUBTRACT
* MULTIPLE
/ DIVIDE
''')


opr=input("Choose an operater: ")
if opr=="+":
    print("The result of operation is",num1+num2)
elif opr=="-":
    print("The result of operation is",num1-num2)
elif opr=="*":
    print("The result of operation is",num1*num2)
elif opr=="/":
    print("The result of operation is",num1/num2)
else:
    print("invalid operator")
