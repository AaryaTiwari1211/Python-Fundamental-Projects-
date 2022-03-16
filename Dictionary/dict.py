import json
from difflib import get_close_matches
dict= json.load(open('Dictionary\data.json'))
def search():
    search=input("Search: ")
    search=search.lower()
    
    if search in dict:
        print(dict[search])
    elif len(get_close_matches(search,dict.keys())) > 0:
        yes_no = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(search, dict.keys())[0])
        yes_no=yes_no.lower()
        if yes_no=="y":
            print(dict[get_close_matches(search, dict.keys())[0]])
        else:
            print("This word is invalid please choose a valid word")

    
search()
        
        
    
    


    
