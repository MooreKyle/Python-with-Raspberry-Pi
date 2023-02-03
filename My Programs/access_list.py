#access_list.py

price_list = [1.99,3.45,29.99,42.95]
print(price_list[-1]) # last item
print(price_list[-2]) # next to the last item
try:
    print(price_list[-10])
except IndexError:
    print("index out of range")
