"""
Challenge 1. Get Prime factors of input.
"""

def primefactors_of(number: int):
    """
    Returns factors of number.
        Parameters:
            number(int): integer
    """
    factors = list()
    least_factor = 2
    while number != 1:
        if (number % least_factor) == 0:
            factors.append(least_factor)
            number = number // least_factor
        else:
            least_factor += 1
    print(factors)

    


primefactors_of(13)
