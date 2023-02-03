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

    print(sold_list)
    sold_list.sort() # sort list in ascending order
    print(sold_list)
    sold_list.reverse() # sort list in descending order
    print(sold_list)
    print(student_list)
    student_list.sort() # sort in alphabetic order
    print(student_list)
    student_list.sort(reverse=True)
    # sort in reverse alphabetic order
    print(student_list)

main()
