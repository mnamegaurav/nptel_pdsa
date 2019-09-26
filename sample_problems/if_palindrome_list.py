def mypalindrome(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(l[0:]==l[-1::-1])