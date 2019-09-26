#1. Strictly increasing absolute differences

def expanding(l):
    diff = []
    
    for i in range(1,len(l)):
        diff.append(abs(l[i]-l[i-1]))
    
    
    check = 0
    for i in range(1,len(diff)):
        if diff[i] > diff[i-1]:
            check+=1
        else:
            return False
    if check == len(diff)-1:
        return True
    
    
    sign = []
    for i in range(1,len(diff)):
        sign.append(diff[i]-diff[i-1])
    rtrn = True
    for s in sign:
        if s <= 0:
            rtrn = False
    return rtrn
        
#2. Strictly Increasing and Decreasing absolute differences in alternative order

def accordian(l):
    if len(l) <= 2:
        return False
    
    diff = []
    
    for i in range(1,len(l)):
        diff.append(abs(l[i]-l[i-1]))
    
    rtrn = False
    for i in range(1,len(diff)-1):
        if diff[i] > diff[i-1]:
            if diff[i+1] < diff[i]:
                rtrn = True
            else:
                return False
        elif diff[i] < diff[i-1]:
            if diff[i+1] > diff[i]:
                rtrn = True
            else:
                return False
        else:
            return False
    return rtrn
        
#3. Rotate a square matrix by 90 degree in clockwise

def rotate(m):
    new_m = [e[:] for e in m]
    N = len(m)
    
    for i in range(0,N):
        for j in range(0,N):
            new_m[j][N-1-i] = m[i][j]
    return new_m