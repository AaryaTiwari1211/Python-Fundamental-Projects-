def vowels():
    word = input("Enter any word with vowels: ")
    word = word.lower()
    count = 0
    for i in word:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            count+=1
            
    if count==0:
            print("This Word has no vowel")
    else:
            print("Total number of vowels are " +str(count))
            
vowels()
