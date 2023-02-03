#Project_Four - Functions
#Kyle Moore - 6-24-19

#libraries
from sense_hat import SenseHat
from time import sleep
import smtplib
from email.mime.text import MIMEText



#Function: compute_discount
def compute_discount(cost:float,member:bool):
    if member:
        mem_discount = 0.10
        print("You are a member. Thus, you will receive a 10% discount. ")
    else:
        mem_discount = 0
        print("You are not a member. So... no discount for you! Did you get the reference? But seriously, no discount. ")

    print("Today is Cyber Tuesday, so all customers will get a 5% discount. ")
    tue_discount = 0.05

    discount = tue_discount + mem_discount
    discounted_cost = cost - (cost * discount)
    return discounted_cost

#Function: clubmember_card
def clubmember_card(club_card:int):
    if club_card == 100 or club_card == 200:
          num_classes = (club_card / 20)
    elif club_card == 300 or club_card == 500:
          num_classes = ((club_card + 15) / 15)
    else:
        pass
    return num_classes

#Function: draw_pattern
def draw_pattern(x1:int,y1:int,x2:int,y2:int,s):
    s.set_pixel(x1,y1,0,0,255) #x1,y1,red,green,blue
    sleep(2)
    s.clear()
    s.set_pixel(x2,y2,0,0,255) #x2,y2,red,green,blue
    sleep(2)
    s.clear()

#Function: data_center_monitor
def data_center_monitor(min_temp:float,max_temp:float,min_humidity:float,max_humidity:float,email_address:str,s:object):
    try:
        monitoring = True
        while monitoring is True:
            fahrenheit = sense.get_temperature
            print(fahrenheit)
            sleep(1)
            
            if temperature not in range(min_temp,max_temp) or humidity not in range(min_humidity,max_humidity):
                fromaddr = "Oneup4klm@gmail.com"
                toaddr = "Oneup4klm@gmail.com"
                username = "Oneup4klm@gmail.com"
                password = "Coolguy3210"
                msg = MIMEText("Warning: The max and min temperature or the max and min humidity recorded is out of range! ")
                msg['Subject'] = 'Warning: Temperature & Humidity'
                msg['To'] = "Oneup4klm@gmail.com"
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                server.login(username,password)
                server.send_message(msg)
                server.quit()
    #Gracefully exit using Ctrl+c
    except KeyboardInterrupt:
        print("Exiting... ")
        sleep(3)

#Function: multi_comp
def multi_comp(value_one:float,value_two:float):
    product = value_one * value_two
    sum = sum(value_one + value_two)
    expon_result = value_one**value_two

    return product,sum,expon_result

#Function: compute_balance
def compute_balance(float(current_balance=1000),float(payment=20)):
    current_balance = current_balance - payment

    if current_balance > 0:
        return "balance owed", current_balance
    elif current_balance < 0:
        return "credit", -current_balance
    elif current_balance == 0:
        return "paid in full", 0

#Function: find_sum
def find_sum(lower_param:int,upper_param:int):
    for l in range(len(lower_param,upper_param)):
        total = sum(len(lower_param + upper_param))
    return total



#main
def main():
    print("Kyle Moore\n\n")

    discounted_cost = compute_discount(150.78,member=True)
    print("The discounted cost is" + format(discounted_cost,'0.2f'))
    discounted_cost = compute_discount(98.23,member=False)
    print("The discounted cost is" + format(discounted_cost,'0.2f'))

    num_classes = clubmember_card(100)
    print("The number of classes you can complete is",num_classes)
    num_classes = clubmember_card(500)
    print("The number of classes you can complete is",num_classes)

    sense = SenseHat()
    sense.clear() #Fresh Start

    draw_pattern(4,5,7,2,sense)

    data_center_monitor(70,90,40,55,Oneup4klm@gmail.com,sense)

    product,sum,expon_result = multi_comp(5,-2)
    print("The product is",product + ". The sum is",sum + ". The exponential result is",expon_result)
    product,sum,expon_result = multi_comp(3,4)
    print("The product is",product + ". The sum is",sum + ". The exponential result is",expon_result)

    text,value = compute_balance(500,payment)
    text = str(text)
    value = float(value)
    print(text,value)
    text,value = compute_balance(current_balance,1100)
    text = str(text)
    value = float(value)
    print(text,value)

    total = find_sum(5,10)
    print("The sum is",total)

main() #Call main
