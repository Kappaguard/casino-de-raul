import math 

a=23 # int(input('1 число: '))
b=32 # int(input('2 число: '))

def euclid(a1,b2):
    """Осуществляет алгоритм Евклида для целых чисел"""
    dels=[]
    if a==0:
        return a1
    elif b==0:
        return b2   
    
    y= min (a1,b2)
    x= max(a1,b2)
    r= 0
    p=0

    while (x > 0):
        p=r
        r = x % y
        if r==0:
           # print(x,p,r)
            break
        x = (x // y)*y
        y= r
    if p==0:
        return min(a1,b2)
    elif (a1 % p !=0) or (b2 % p !=0):
        p=min(euclid(a1,p), euclid(b2,p))
        return(p)
    else:
        return(p)


print(euclid(a,b))