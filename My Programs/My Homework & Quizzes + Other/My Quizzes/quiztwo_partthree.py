#quiztwo_partthree.py
#Kyle Moore - 6-5-19



#main
def main():
    #Call function: retail_price_finder
    retail_price = retail_price_finder(wholesale_price,percent_markup)

    #Call function: retail_price_finder & return retail_price
    print("The retail price is: " + format(retail_price,"0.2f"))



#Function: retail_price_finder
def retail_price_finder(wholesale_price,percent_markup):
    #Call function: retail_price_finder
    retail_price_finder(100.0,25)

    #compute expression & return retail_price
    return wholesale_price + (wholesale_price * (percent_markup/100.0))

main()
