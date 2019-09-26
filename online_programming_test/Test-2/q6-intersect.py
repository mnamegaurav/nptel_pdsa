def intersect(l1,l2):
    intersect_list = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                intersect_list.append(l1[i])
                
    return list(set(intersect_list))