def translator(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter in "AEIOU":
             translation=translation + "G"
            else:
             translation=translation +"g"
        else:
            translation=translation+letter
    return translation
print(translator(input("Enter a phrase: ")))


