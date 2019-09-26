def maxbad(l):
  mymax = 0
  for i in range(len(l)):
    if l[i] > mymax:
       mymax = l[i]
  return(mymax)

'''
[-1,-2,-3]
'''