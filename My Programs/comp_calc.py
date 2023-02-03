#comp_calc.py

# """ or ''' = Multi-Line Comment
def commission_calc(sales:float=100,comm_rate:int=10)->float:
    """
    This function computes the commission based upon the sales
    and the commission rate.
    Two floats are the parameters.
    The function returns a float.
    Discuss algorithm.
    """
    if sales > 1000:
        commission = sales*(comm_rate/100) + 50
    elif sales >= 500:
        commission = sales*(comm_rate/100) + 25
    else:
        commission = sales*(comm_rate/100)
    return commission
