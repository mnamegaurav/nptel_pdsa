import itertools
def subsequence(l1,l):
    for i in range(1,len(l)+1):
        p = list(itertools.combinations(l,i))
        for e in p:
            if tuple(l1)==e:
                return True
    else:
        return False

# subsequence([2,2,5],[2,2,3,4,5])
# subsequence([2,3,4],[2,2,3,4,5])
# subsequence([2,4,4],[2,2,3,4,5])
# subsequence([2,4,3],[2,2,3,4,5])
# subsequence([2,2,5],[2,2,3,4,5])
# subsequence([2,4,4],[2,2,3,4,5])