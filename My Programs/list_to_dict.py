#list_to_dict.py

def main():
    student_list = ["Mary","Mark","Tony"]
    credit_list = [50,57,63]

    student_dict = dict(zip(student_list,credit_list))
    for s,c in student_dict.items():
        print(s + " has " + str(c) + " credits")
    print(student_dict)

    print(max(student_dict.values()))
    print(min(student_dict.values()))
    credit_list[0] = 55
    for v in credit_list:
        print(v)
    student_dict["Mary"] = 65
    for v in student_dict.values():
        print(v)
    student_dict.update({"Toni":70,"Mary":75,"Tony":0})
    print("after update() method was called")
    for s,c in student_dict.items():
        print(s + " has" + str(c) + " credits")

main()
