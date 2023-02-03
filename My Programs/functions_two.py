#functions_two.py
def sales_compute(number_sold,price_each=5.00,tax_rate=.06):
    total = number_sold * price_each
    tax = (tax_rate/100) * total
    return total,tax

def main():
    sold = int(input("Enter the number of items sold "))
    price = float(input("Enter the price of each item "))
    t_rate = float(input("Enter the tax rate "))

    # positional arguments
    result,tax_amount = sales_compute(sold,price,t_rate)
    print(result)
    print(tax_amount)
    result,tax_amount = sales_compute(sold,price)
    print(result)
    print(tax_amount)
    result,tax_amount = sales_compute(sold)
    print(result)
    print(tax_amount)
    # one position argument and one keyword argument
    result,tax_amount = sales_compute(sold,tax_rate=t_rate)
    print(result)
    print(tax_amount)
    # one position argument and two keyword arguments
    result,tax_amount = sales_compute(sold,tax_rate=t_rate,\
                                      price_each=price)
    print(result)
    print(tax_amount)
    #error - positional argument is after a keyword argument
    #result,tax_amount = sales_compute(sold,tax_rate=t_rate,price)
main()
