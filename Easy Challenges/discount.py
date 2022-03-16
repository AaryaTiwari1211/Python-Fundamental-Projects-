

def get_discounted_price():
    full_price = float(input("Enter the price of the item: "))
    discount= float(input("Enter the discount you want to apply: "))
    discounted_price=  full_price-((full_price*discount)/100)
    print (str(discounted_price))


get_discounted_price()