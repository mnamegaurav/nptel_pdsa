def lexsortbad(l):
    for k in range(2):
        for j in range(len(l)-1):
            for i in range(len(l)-1):
                if l[i][k] > l[i+1][k]:
                    (l[i],l[i+1]) = (l[i+1],l[i])
    return(l)

# this function is wrong for every value
lexsortbad([(232,221),(228,233)])