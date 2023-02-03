#list_one.py

city_list = []
temp_list = [98.6,212.0,37.078.4]
occur_list = [0] * 10

for i in range(len(temp_list)):
    print(temp_list[i])

i = 0
while i < len(temp_list):
    print(temp_list[i])
    i += 1

for t in temp_list:
    print(t)
occur_list[0] = 15
occur_list[1] = 13
for occur in occur_list:
    print(occur)
#city_list[0] = "Lake Worth" # no item at index 0
city = input("Enter a city")
while city.lower() != "quit":
    city_list.append(city)
    city = input("Enter a city, enter quit to exit")
for c in city_list:
    print(c)
i = 0
while i < len(temp_list): # OK, sets the value of all items
    temp_list[i] = float(input("Enter a temperature "))
    i += 1
temp = float(input("Enter a temperature "))
while temp > 0: #OK, appends a new item
    temp_list.append(temp)
    temp = float(input("Enter a temperature "))
print("There are {0:5d} items in the temp_list".format(len(temp_list)))
temp_list.insert(0,45.6) # add 45.6 to the beginning of the temp_list
temp_list.append("bye")
for i in range(len(temp_list)):
    print(temp_list[i])
"""
i = 0
while i < len(temp_list): #BAD, the loop will not end
    temp_list.append(float(input("Enter a temperature ")))
    i += 1
"""
