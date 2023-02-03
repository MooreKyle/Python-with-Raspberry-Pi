#sum_only_even.py

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

main()
