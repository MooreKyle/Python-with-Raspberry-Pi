#quiztwo_parttwo.py
#Kyle Moore - 6-5-19



#main
def main():
    #Call function: equation_evaluate with appropriate arguments
    y = equation_evaluate(4.0,4.0,-1.5,0)

    #(1) Print returned result w/ 1 decimal place of precision
    print("The first result is: " + format(y,"0.1f"))

    #Call function: equation_evaluate AGAIN with appropriate arguments
    y = equation_evaluate(4.0,2.0,-1.5,10.5)
    
    #(2) Print returned result w/ 1 decimal place of precision
    print("The second result is: " + format(y,"0.1f"))



#Function: equation_evaluate
def equation_evaluate(a,b,c,x):
    y = a * x * x + b * x + c
    return y

main() #Call main
