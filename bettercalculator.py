# Using if else statements 



num1= input("Enter a Number: ")
num2= input("Enter another Number: ")

arithematic= input("Enter the operation you want(+,-,*,/): ")

if arithematic == "+":
    print(int(num1)+int(num2))
elif arithematic == "-":
     print(int(num1)-int(num2))
elif arithematic == "*":
    print(int(num1)*int(num2))
elif arithematic == "/":
    print (int(num1)/int(num2))
else:
    print("Please enter a valid operator")






