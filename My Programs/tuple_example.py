#tuple_example.py

def main():
    price_tuple = 1.99,2.49,4.70
    course_tuple = ("COP 2840","COP 2800","COP 1220")
    course_tuple_2 = ("CTS 2447",) # tuple with one item
    course_string = "CTS 2447"

    for c in course_tuple:
        print(c)

    for i in range(len(course_tuple)):
        print(course_tuple[i])
    # concatenate tuples to make a new tuple
    all_courses_tuple = course_tuple + course_tuple_2
    print(all_courses_tuple)
    #price_tuple.sort() # cannot sort a tuple
    # tuples are immutable
    price_list = list(price_tuple) # returns a list from the items in a tuple
    price_list.sort()
    price_tuple = tuple(price_list) # returns a tuple from the items in a list
    print(price_tuple)
    print(sum(price_tuple))
    print(min(price_tuple))
    print(max(price_tuple))
    print(len(price_tuple))
    # price_tuple[0] = 10.0 # cannot assign a value to an item in a tuple
    
main()
