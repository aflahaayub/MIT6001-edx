def mult_iter(a,b):
    total = 0
    while a > 0:
        total+=b
        a-=1
    return total

print(mult_iter(2, 5))