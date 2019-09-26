def thirdmin(l):
  (mymin,mysecondmin,mythirdmin) = (1000000,1000000,1000000)
  for i in range(len(l)):
    # Your code below this line
    curr_num = l[i]
    while curr_num < l[i-1] and i-1>=0:
      l[i-1], l[i] = l[i],l[i-1]
      i-=1
    else:
      mythirdmin = l[2]
  
    # Your code above this line
  return(mythirdmin)