a_custom=25 # int(input('1 число: '))
b_custom=5 # int(input('2 число: '))

def euclid(a_1,b_2):
    """Осуществляет алгоритм Евклида для целых чисел"""

    if a_1==0:
        return b_2
    elif b_2==0:
        return a_1

    y= min (a_1,b_2)
    x= max(a_1,b_2)
    r_ost= 0
    p_ost=0

    while x > 0:
        p_ost=r_ost
        r_ost = x % y
        if r_ost==0:
            break
        x = (x // y)*y
        y= r_ost
    if p_ost==0:
        return min(a_1,b_2)
    elif (a_1 % p_ost !=0) or (b_2 % p_ost !=0):
        p_ost=min(euclid(a_1,p_ost), euclid(b_2,p_ost))
        return(p_ost)
    else:
        return(p_ost)


print(euclid(a_custom,b_custom))

