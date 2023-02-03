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

main()
