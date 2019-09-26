def nondecreasing(l):
    if l==[] or len(l) == 1:
        return(True)
    else:
        return nondecreasing(l[1:]) if l[0] <= l[1] else False

nondecreasing([1,2,3])