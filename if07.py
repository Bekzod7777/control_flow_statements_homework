def main(a):
    if a%2>0:
        return "positive odd number"
    if (a+1)%2>0:
        return "positive even number"
    if a%2<0:
        return "negative odd number"
    if (a+1)%2<0:
        return "negative even number"
    else:
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
    