# Creating a list
mylist = [
    "apple",
    "banana",
    "grapes",
    "mango",
    "lichi",
    
]
# Printing the list
print(mylist)

# Storing the list in a variable
item = mylist[0]
print(item)

# Adding items to list using 'append' function
mylist.append("lemon")
print(mylist)

# Printing number of items in a list using 'len' function
print(len(mylist))

# Replacing items using 'insert' function
mylist.insert(1,"blueberry")
print(mylist)

# Finding last value using 'pop' function
print(mylist.pop())

# Removing items using 'remove' function
mylist.remove("banana")
print(mylist)

# Remove all elements using 'clear' function
mylist.clear()

# Reverse the order of elements using 'reverse' function
mylist.reverse()
print(mylist)

# Sorting numbers using 'sort' function
num = [4,7,8,90,67,45,23,56,85,49]

num.sort()
print(num)

# Printing same numbers repeatedly using multiplication
num1 = [90] * 5
print(num1)

# Adding two lists
new_list = num + mylist
print(new_list)

# Printing range of items using colon
a = num[4:8]
print(a)
# Printing alternate numbers using two colons

b=num[::2]
print(b)

# Making a copy of a list [3 methods]

numbers = num.copy()
print(numbers)
numbers = list(num)
print(numbers)
numbers = num[:]
print(numbers)

# List Comprehension

aa = [1,2,3,4,5,6]
bb = [i*i for i in aa]
print (aa)
print (bb)





