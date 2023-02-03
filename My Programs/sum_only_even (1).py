#sum_only_even.py
from sense_hat import SenseHat
def main():
    value = 1
    total = 0
    while value > 0:
        value = int(input("Enter a number "))
        if value%2 != 0:  # True, if the value is odd
            continue
            # skip the remaining statements
            # go to the next iteration
        total = total + value
    print(total)
    sense = SenseHat()
    p = 1
    count = 1
    while p > 0:
        p = sense.get_pressure()
        if p == 0:
            print("pressure not measured")
            p = 1
            continue # go to the next iteration
        print(p)
        count += 1
        if count > 10:
            break # exit loop
main()
