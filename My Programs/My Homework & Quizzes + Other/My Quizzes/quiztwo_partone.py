#quiztwo_partone.py
#Kyle Moore - 6-5-19



#Libraries
from sense_hat import SenseHat 
from time import sleep



#main
def main(): #main() body

    sense = SenseHat() #Initialize Sense HAT
    sense.clear() #Fresh Start

    #for loop - Display 8 even values
    a = 0
    even = 2
    for a in range(0,8):
        print(even)
        even += 2
        a += 1

    print("\n")
        
    #while loop - Display 7 varying values
    b = 0
    diff = 16
    while b <= 6:
        print(diff)
        b += 1
        diff -= 3

    #for loop - Scroll Message via Sense HAT
    c = 0
    for c in range(0,3):
        sense.show_message("Loops are fun",scroll_speed=0.05,text_colour=[0,0,255])
        c += 1

    #while loop - Sentinel-Controlled w/ Multiplicative Accummulator
    num = 1
    product = 1
    while num != 0:
        num = int(input("\nPlease enter a number: "))
        if num == 0:
            break
        product = product * num
        print("The new product is: ",product)

    #Print final product
    print("The final product is: ",product)

main() #Call main
