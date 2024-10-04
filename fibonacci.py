def Fibonaci(n):
    if n==0 or n ==1:
        return 1
    else:
        return Fibonaci(n-1) + Fibonaci(n-2)

print(Fibonaci(4))