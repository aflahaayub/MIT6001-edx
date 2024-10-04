def iterPower(base, exp):
    total = 1
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    while exp > 0:
        total = total*base
        exp -= 1
    
    return total

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    return base * recurPower(base, exp-1)

print(recurPower(2, 3))