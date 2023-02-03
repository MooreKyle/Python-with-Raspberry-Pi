#list_functions.py

def main():
    sold_list = [3,56,23,10,14,0]
    student_list = ["Lorelei","Enzo","Duc","Tran"]

    minimum = min(sold_list)
    print(minimum)
    print(max(sold_list))
    print(sum(sold_list))

    average = sum(sold_list)/len(sold_list)
    print("average number sold " + str(average))

    sold_list = [3,56,23,10,14,0]
    print("original sold_list")
    print(sold_list)
    sold_list.reverse() # sort in reverse order
    print("after reverse() method is called")
    print(sold_list)
    print("after sort() method is called")
    sold_list.sort() # sort in ascending order
    print(sold_list)
    print("after sort(reverse=True) " + \
          "method is called")
    sold_list.sort(reverse=True)
    # sort in descending order
    print(sold_list)
    sold_list.clear()
    print("after clear() method is called")
    print(sold_list)




    print(student_list)
    student_list.sort() # sort in alphabetic order
    print(student_list)
    student_list.sort(reverse=True)
    # sort in reverse alphabetic order
    print(student_list)

main()
