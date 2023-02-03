#list_part_three.py
from sense_hat import SenseHat
from time import sleep

def main():
    city_list = ["Lake Worth","Boca Raton","Miami", "Fort Lauderdale",
                 "Boynton Beach"]
    city_list_2 = ["Delray Beach","Orlando"]
    # del() function
    try:
        index_remove = int(input("Enter the index of the element to remove"))
        del(city_list[index_remove])
        print("item removed")
    except IndexError:
        print("could not remove element")
    except ValueError:
        print("non-integer index")
    for c in city_list: 
        print(c)
    # remove() method
    try:
        city = input("Enter the city to remove").title()
        city_list.remove(city)
        print("item removed")
    except IndexError:
        print("could not remove element")
    except ValueError:
        print("could not remove element")
    except Exception:
        print("could not remove element")
        
    for c in city_list:
        print(c)
    # remove() method; test before attempting to remove item
    city = input("Enter the city to remove").title()
    if city in city_list:
        city_list.remove(city)
        print("item removed")

    for c in city_list:
        print(c)
    # pop() method
    try:
        index_remove = int(input("Enter the index of the element to remove"))
        value = city_list.pop(index_remove)
        print("item removed " + str(value))
    except IndexError:
        print("could not remove element")

main()





