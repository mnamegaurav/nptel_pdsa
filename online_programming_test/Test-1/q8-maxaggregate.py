from collections import defaultdict
def maxaggregate(l):
    result = defaultdict(list) 
    for i, j in l:
        result[i].append(j) 
    result = dict(result)
    aggregate_score = {}
    for k, v in result.items():
        aggregate_score.update({k:sum(v)})
    itemMaxValue = max(aggregate_score.items(), key=lambda x: x[1])
    listOfKeys = list()
    for key, value in aggregate_score.items():
        if value == itemMaxValue[1]:
            listOfKeys.append(key)
    listOfKeys.sort()
    return listOfKeys
    
max = maxaggregate([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',22),('Ashwin',47)])
print(max)