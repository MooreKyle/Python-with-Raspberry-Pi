#cost_compute.py

def main():
    try:
       price = float(input("What is the cost of the soda? "))
    except ValueError:
       price = 1.99
    finally:
       pass

    try:
        number_sold = int(input("How many sodas do you want? "))
    except ValueError:
        number_sold = 1
    finally:
       pass
    cost = price * number_sold
    print("Your total cost is {:10.3e}".format(cost))
    print("Your total cost is {:10,.2f}".format(cost))
    msg = "Your total cost is {:10,.2f}".format(cost)
    print(msg)
    print("You ordered {:5d} sodas which cost {:7.2f} each".\
        format(number_sold,price))
    print("You ordered {0:5d} sodas which cost {1:7.2f} each".\
        format(number_sold,price))
    print("Price {1:7.2f} number_sold {0:5d}".\
        format(number_sold,price))

main()
