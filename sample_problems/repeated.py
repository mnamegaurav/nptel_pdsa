def repeated(l):
    repeated_values = []
    for e in l:
        count = l.count(e)
        if count>1:
            repeated_values.append(e)
            print(set(repeated_values))
    return len(set(repeated_values))

l = [1,17,22,17,23,17,18,19,20,17,23,45,17]
print(repeated(l))