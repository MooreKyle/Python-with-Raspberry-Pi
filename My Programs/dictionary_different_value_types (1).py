#dictionary_different_value_types.py

def main():
    itineary_dict = {"Belgium":"Tuesday",234:29938.87,
                     901:["Candy Corn", 333, 2.908],(2,1):109,
                     "London":{"hotel":200.00,"food":56.34,
                               "tickets":102.33,"transportation":34.22}}
    for key in itineary_dict.keys():
        print(key)
    for value in itineary_dict.values():
        if isinstance(value,float):
            print(format(value,".2f"))
        elif isinstance(value,int):
            print(format(value,"5d")) 
        elif isinstance(value,str):
            print(value)
        elif isinstance(value,tuple) or isinstance(value,list):
            for v in value:
                print(v)
        elif isinstance(value,dict):
            for k,v in value.items():
                print(str(k) + "=" + str(v))

main()
