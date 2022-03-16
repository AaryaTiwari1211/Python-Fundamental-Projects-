import random
import math


lower_range = int(input("Enter the lower number:-"))
upper_range = int(input("Enter the upper number:-"))



x = random.randint(lower_range,upper_range)
print("\nYou have only", round(math.log(upper_range - lower_range + 1, 2)), "chances to guess the correct number")

count = 0

while count < math.log(upper_range - lower_range + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))

    if x==guess:
        print("Congrats you have too much time in your hands to be playing this game. Please leave immediately")
        break
    elif x > guess:
        print("You have guessed wrong noob!!!! The number you chose is smaller than the correct number")
    elif x < guess:
        print("You guessed wrong noob!!! The number you chose is higher than the correct number")
    
    if count >= math.log(upper_range- lower_range + 1, 2):
        print("\nThe number is %d" % x)
        print("Go to Hell Sucker ")
        
 
   