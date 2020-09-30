def divide(dividend, divisor):
    """
    Function that dives two numbers
    Args:
        dividend (float): number to divide from
        divisor (float): Number to divide with

    Return:
        quotent (int)
        remainder (int)
    
    Raises:
        ValueError (division_by_zero): If `divisor` is zero
    """
    if divisor == 0:
        raise ValueError('division_by_zero')
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    """
    Divide two number and collect two return values
    Args: 
    x (decimal): number to divide from
    y (decimal): Number to divide with

    """
    (q, r) = divide(x,y)
    # print the quotient, remainder
    print q, r