#splitjoin_list.py

def main():
    sold_list = [3,56,23,10,14,0]
    student_list = ["Lorelei","Enzo","Duc","Tran"]

    s1,s2,s3,s4,s5,s5 = sold_list
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)

    course_str = "COP 1220, COP 2800, COP 1030, COP 2700"
    course_list = course_str.split(",") # , is the delimiter
    for c in course_list:
        print(c)
    course_str_2 = "|".join(course_list) # | is the delimiter
    print(course_str_2)

main()
