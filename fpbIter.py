def gcdIter(a,b):
    fpb = 1
    prima = 2
    bigger = 0
    lower = 0

    if a>b:
        bigger = a
        lower = b
    elif b>a:
        bigger = b
        lower = a
    else:
        return a

    while bigger >0 and lower>0:
        if bigger%lower==0:
            return lower
        else:
            if lower%prima == 0 and bigger%prima==0:
                fpb = fpb*prima
                lower = lower/prima 
                bigger = bigger/prima
            else:
                prima+=1
            
            if lower == 1:
                return fpb
            
            if lower < prima and bigger < prima:
                return fpb
                
print(gcdIter(150, 190))