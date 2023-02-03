#car_dict_example.py
class Car():
    
    def __init__(self,make="",model="",year="",owner=""):
        self.make = make
        self.model = model
        self.year = year
        self.owner = owner
        # super. press tab to see the inherited methods

    def __str__(self):
        return "owner " + self.owner + " make " + self.make + \
               " year " + self.year + " model " + self.model

def main():
    car_dict = {}
    owner_name = input("Enter the owner's name ")
    while owner_name != "exit":
        make = input("Enter the make of the car ")
        model = input("Enter the model")
        year = input("Enter the year of the car ")
        car_dict[owner_name] = Car(make,model,year,owner_name)
        owner_name = input("Enter the owner's name ")
    for c in car_dict.values():
        print(c)

main()
