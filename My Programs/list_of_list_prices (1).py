#list_of_list_prices.py

import copy

def main():
    price = [[14.95,11.25,14.96],[9.95,2.99,0.99]]
    sold_list = [10,20,30,0]
    print(id(sold_list))
    new_sold_list = sold_list # shallow copy
    print(id(new_sold_list))
    new_sold_list[3] = 100
    # new_sold_list refers to the same location in memory
    # of sold_list
    print(sold_list)
    
    sold_list_2 = [] + sold_list # makes a copy
    sold_list_2[1] = 15
    print(id(sold_list_2))
    print(sold_list)
    
    sold_list_3 = list(sold_list)
    # makes an independent copy; ints are immutable
    sold_list_3[2] = 42
    print(sold_list)
    
    new_price = price # shallow copy

    price_list_2 = list(price)
    # will not make an independent copy
    # of a list of lists; lists are immutable
    price_list_2[0][0] = 199.99
    print(price)

    price_list_3 = copy.deepcopy(price)
    # The deepcopy method makes an independent copy.
    price_list_3[0][0] = 8.88
    print(price)

    # This also makes an independent copy.
    price_list_4 = []
    for row in range(len(price)):
        price_list_4.append([0]*len(price[row]))
    for row in range(len(price)):
        for col in range(len(price[row])):
            price_list_4[row][col] = price[row][col]
    print(price_list_4)
main()
