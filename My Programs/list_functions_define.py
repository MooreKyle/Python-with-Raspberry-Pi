#list_functions_define.py

def update_cost(cost_list:list,mark_up:float)->None:
    for i in range(len(cost_list)):
        cost_list[i] = (1 + mark_up/100)*cost_list[i]


def update_cost_2(cost_list:list,mark_up:float)->list:
    updated_list = [0]*len(cost_list)
    for i in range(len(cost_list)):
        updated_list[i] = (1 + mark_up/100)*cost_list[i]
    return updated_list


def main():
    grocery_list = [3.55,10.77,0.99,15.4,23.44]
    update_cost(grocery_list,10)
    print(grocery_list)
    grocery_list = [3.55,10.77,0.99,15.4,23.44]
    retail_list = update_cost_2(grocery_list,10)
    print(retail_list)
    print(grocery_list)

main()
