def sublist(l1,l2):
    for i in range(len(l2)):
        if l1 == l2[i:i+len(l1)]:
            return True
    else:
        return True

l1=[2,3,4]
l2=[1,2,3,4,5]
sublist(l1,l2)