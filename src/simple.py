import math


# changes that doesn't change code
def check_simple(num):
    for divider in range(2, math.floor(num**0.5)):
        if not (num % divider):
            return False
    return True
