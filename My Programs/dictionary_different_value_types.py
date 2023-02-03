#dictionary_different_value_types.py

def main():
    temperature = 87.3
    count = 1
    food_list = ["pizza","sub","taco"]
    fee_tuple = (34.99,11.23,33.44,33.90)
    name_str = "Your name"

    data_list = [temperature,count,food_list,fee_tuple,name_str]
    for d in data_list:
        if isinstance(d,float): #isinstance checks the data type to match up
            print(str(d) + " is a float")
        elif isinstance(d,int):
            print(str(d) + " is an int")
        elif isinstance(d,str):
            print(d + " is a string")
        elif isinstance(d,tuple):
            print(str(d) + " is a tuple")
        elif isinstance(d,list):
            print(str(d) + " is a list")
        elif isinstance(d,dict):
            print(str(d) + " is a dictionary")

main()
