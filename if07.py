def main(a):
    if a%2>0:
        return "positive odd number"
    elif (a+1)%2>0:
        return "positive even number"
    elif a%2<0:
        return "positive odd number"
    elif (a+1)%2<0:
        return "positive even number"
    else a==0:
        return "the number is zero"
    
    


    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    