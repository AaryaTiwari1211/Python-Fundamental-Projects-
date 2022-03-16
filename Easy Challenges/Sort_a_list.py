list = [1,4,2,7,8,5,9,30,56,45,37,90,789,56,567,56]

def list_sort(list,order):
    list_asc = list.sort()
    list_desc = list.sort(reverse=True) 
    if order == "asc":
        print (list_asc)
    elif order == "desc":
        print(list_desc)
    else:
        print(list)

list_sort(list, "asc")