def applyToEach(L, f): 
    for i in range(len(L)):
        L[i] = f(L[i]) # if L = [-1], then f is abs, the list will be [1]
    return L

print(applyToEach([1,-2,4,0.5], abs))
