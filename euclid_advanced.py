A_CONST=903 # int(input('1 число: '))
B_CONST=1435 # int(input('2 число: '))

def euclid_advanced(a_1,b_2):
    """Осуществляет расширенный алгоритм Евклида для целых чисел"""

    if a_1==0:
        return b_2
    elif b_2==0:
        return a_1

    y= min (a_1,b_2)
    x= max(a_1,b_2)
    r_ost= 0
    p_ost=0
    c_ount=0
    ost_atki=[]

    while x > 0:
        p_ost=r_ost
        r_ost = x % y
        c_ount+=1
        # ost_atki[c_ount]=p_ost — на этом этапе завершил сеанс выполнения дз
        if r_ost==0:
            break
        x = (x // y)*y
        y= r_ost

    if p_ost==0:
        p_ost = min(a_1,b_2)
    elif (a_1 % p_ost !=0) or (b_2 % p_ost !=0):
        p_ost=min(euclid_advanced(a_1,p_ost), euclid_advanced(b_2,p_ost))


    bezu= p_ost
    return bezu

print(euclid_advanced(A_CONST,B_CONST))