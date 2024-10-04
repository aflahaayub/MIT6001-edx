def gcdRecur(a,b):
    if b>a:
        b = b-a
        a = b+a
    if a%b == 0:
        return b
    
    return gcdRecur(b, a%b)

print(gcdRecur(150, 190))