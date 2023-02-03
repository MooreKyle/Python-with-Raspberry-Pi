#list_part_two.py
from sense_hat import SenseHat
from time import sleep

def main():
    city_list = ["Lake Worth","Boca Raton","Miami", "Fort Lauderdale",
                 "Boynton Beach"]
    city_list_2 = ["Delray Beach","Orlando"]
    list_s = city_list[2:4] # start at index 2, slice to index 3 (4-1 = 3)
    print(list_s)
    list_s_2 = city_list[0:2] # start at index 0, slice to index 1 (2-1 = 1)
    print(list_s_2)
    list_s_2[0] = "Tampa"
    print(list_s_2)
    print(city_list)
    str_s_3 = str(city_list[0:1])[7:12]
    print(str_s_3)
    list_s_4 = city_list[:2]
    # start at index 0, slice to index 1 (2-1 = 1)
    print(list_s_4)
    list_s_5 = city_list[2:]
    # start at index 2, slice to the end of the list
    print(list_s_5)
    complete_list = city_list + city_list_2
    for c in complete_list:
        print(c)
    i = 0
    while i < len(complete_list):
        print(complete_list[i])
        i += 1
    temp_list = [212.0,32.0,98.6]
    city_temp_list = city_list + temp_list
    for i in range(len(city_temp_list)):
        print(city_temp_list[i])
    
main()


