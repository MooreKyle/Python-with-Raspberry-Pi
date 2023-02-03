#dictionary_declare_initialize.py

def main():
    comp_dict = {}
    electronic_dict = {"capacitor":3.29,"LED":2.99}
    electronic_dict["resistor"] = 0.99 # adds a new item
    electronic_dict["capacitor"] = 3.49 # update value (can update values, but not keys)
    print("values in electronic_dict")
    for e in electronic_dict.values():
        print(e)
    print("keys in electronic_dict")
    for ke in electronic_dict.keys():
        print(ke)
    for ke,e in electronic_dict.items():
        print("key = " + ke + " value = " + str(e))
    try:
        find = input("Enter the key ")
        print(electronic_dict[find])
    except KeyError:
        print("The key was not found")
    find = input("Enter the key ")
    if find in electronic_dict:
        print(electronic_dict[find])
    else:
        print("The key was not found")
    print(type(electronic_dict.items()))
    print(type(electronic_dict.keys()))
    comp_str = input("Enter a component ") # priming read
    while comp_str != "exit":
        comp_price = float(input("Enter a price "))
        comp_dict[comp_str] = comp_price
        comp_str = input("Enter a component ") # loop read
    total = sum(comp_dict.values())
    print("total of all components {0:.2f}".format(total))
    print(comp_dict)

main()
