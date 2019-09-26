#Domino Solitaire

n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

diff = []
diff.append(abs(l1[0]-l2[0])) # for first column / for 1 column grid
diff.append(max(diff[0]+abs(l1[1]-l2[1]),abs(l1[0]-l1[1])+abs(l2[0]-l2[1]))) # for 2 column grid

i=2
while i<len(l1):
    diff.append(max(diff[i-1]+abs(l1[i]-l2[i]),diff[i-2]+abs(l1[i]-l1[i-1])+abs(l2[i]-l2[i-1])))
    i+=1

print(diff[-1])