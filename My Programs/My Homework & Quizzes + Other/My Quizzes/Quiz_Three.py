#Quiz_Three - Lists&Tuples
#Kyle Moore - 6-12-19

def main():
    software_list = ["Microsoft Office Personal","Quickbooks Pro","TurboTax Premier","LibreOffice"]
    cost_list = [0,0,0,0]
    i = 0
    for i in range(0,4):
        cost_list[i] = float(input("Please enter 4 prices: "))

    cookie_order_list = []
    total = 0
    for c in range(0,6):
        cookie_order_list = int(input("\nPlease enter the number of cookies ordered: "))
        total = total + cookie_order_list
        c += 1
    print("The sum of the cookies ordered is:",total,"\n\n")

    SENTINEL = 0
    num = 0
    while SENTINEL != -1:
        num = int(input("Please continue to enter the number of cookies ordered: "))
        SENTINEL = int(input("Would you like to continue? (Enter any numeric integer to continue, or press -1 to quit): "))
        cookie_order_list.append(num)



    #8.
    cookie_order_list.sort(Reverse=True)
    for c in range(cookie_order_list):
        print(cookie_order_list)

    #9.
    application_list = software_list + cost_list
    while len(application_list):
        print(application_list)

    #10.
    def list_product_function(list_one, list_two):
        total_list = []
        list_one = []
        list_two = []
        total_list = list_one
        total_list = list_one * list_two
        return total_list

    #11.
    a_list = [3,4,9,14]
    b_list = [5,6,99,3]
    list_product_function(a_list, b_list)
    result_list = total_list
    print(result_list)

    #12.
    emp = 3
    items = 4
    work = [[emp][items]] #[row][col]

    #15
    row = 5
    col = 2
    work2 = [[row][col]]
        




main() #Call main
