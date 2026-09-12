"""Problem Description:

You are given an integer n. Your task is to return a sandglass pattern of '*', where the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, until the last row contains a single star. After reaching the smallest width, the pattern then continues with the same number of stars increasing back to 2n - 1. The stars in each row should be centered.

Input:

A single integer n, where 1 <= n <= 100.
Output:

A list of strings where each string represents a row in the sandglass pattern.
Example:

Input: 3
Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']
 
Input: 4
Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
"""

n=3


lst=[]

# reverse Pyramid Pattern
for i in range(n-1):
  str=""
  spc=""
  NStar=(2*(n-i))-1
  spc+=" " * i
  str+="*" * NStar
  lst.append(spc+str+spc)

# Pyramid Pattern
for i in range(n):
  str=""
  spc=""
  Nspace=(n-i)-1
  Nstar=(i*2)+1
  spc+=" " * Nspace
  str+="*" * Nstar
  lst.append(spc+str+spc)



print(lst)
