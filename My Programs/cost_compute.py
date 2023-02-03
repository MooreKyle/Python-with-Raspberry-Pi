#cost_compute.py

def main():
    try:
       price = float(input("What is the cost of the soda? "))
       number_sold = int(input("How many sodas do you want? " ))
    except ValueError:
       price = 1.99
       number_sold = 1
    finally:
       pass

    print("You ordered {:5d} sodas which cost {:7.2f} each".\
        format(number_sold,price))
    print("You ordered {0:5d} sodas which cost {1:7.2f} each".\
        format(number_sold,price))
    print("Price {1:7.2f} number_sold {0:5d}".\
        format(number_sold,price))

main()

print("The total cost of the sodas is: ").\
total = number_sold * price
print(total)
