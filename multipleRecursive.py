def mult_rec(a,b):
    if b==1:
        return a
    return a + mult_rec(a, b-1)