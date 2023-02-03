#new_jersey_state_tax.py

def main():
    income = float(input("Enter the income "))
    if income <= 20000:
        tax = 0.014 * income
    elif income <= 30000:
        tax = 0.014 * 20000 + 0.0165 * (income - 20000)
    elif income <= 45000:
        tax = 0.014 * 20000 + 0.0165 * 10000 + 0.0173 * (income - 30000)
    else:
        tax = (0.014 * 20000 + 0.0165 * 10000 + 0.0173 * 15000 + 0.0227 * (income - 45000))
    print("Your tax is $" + format(tax,".2f"))

main()
