#list_of_list.py

def main():
    work_attended = [[0]*5,[0]*5,[0]*5] # three rows, five columns
    for row in range(len(work_attended)): # number of rows
        for col in range(len(work_attended[row])): # number of columns
            work_attended[row][col] = int(input("hours worked for " +\
                                                str(row) + " day" + str(col)))
    for row in range(len(work_attended)): # number of rows
        for col in range(len(work_attended[row])): # number of columns
            print(format(work_attended[row][col],"2d"),end = " ")
        print()
    total_hours_worked = 0
    for row in range(len(work_attended)): # number of rows
        for col in range(len(work_attended[row])): # number of columns
            total_hours_worked += work_attended[row][col]
    print("total hours for all employees " + str(total_hours_worked))
    emp_number = int(input("Enter the employee number"))
    emp_hours = 0
    for col in range(len(work_attended[emp_number])):   # add code here to find the number of hours worked in the week
        emp_hours += work_attended[emp_number][col]     # for a single employee; use a loop
    print(emp_hours)
    # BONUS HW Points: Write another loop to find the hours worked for a day
    # prompt for day_number; sum down a column
    day_hours = 0
main()
