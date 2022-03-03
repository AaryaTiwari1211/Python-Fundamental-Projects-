def maxnumber (num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print("Num1 is the biggest number")
        return num1
    elif num2>=num1 and num2>=num3:
        print("Num2 is the greatest")
        return num2
    else:
        print("Num3 is the greatest")
        return num3

print(maxnumber(34,45,89))
