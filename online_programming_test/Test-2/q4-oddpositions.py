def oddpositions(l):
  if len(l) <= 1:
    return([])
  else:
    return(
       # Complete the recursive call below this line
l[1::2]
       # Complete the recursive call above this line
    )