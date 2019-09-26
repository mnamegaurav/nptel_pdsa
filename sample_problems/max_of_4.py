def max4(w,x,y,z):
    if w >= x and w >= y and w >= z:
        maximum = w
    elif x >= y and x >= z:
        maximum = x
    elif y >= z:
        maximum = y
    else:
        maximum = z

    return(maximum)

max4(32,12,16,11)