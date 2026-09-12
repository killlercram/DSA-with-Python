"""Problem Description:

You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.

Input:

A single integer n, where 1 <= n <= 100.


Output:

A list of strings where each string represents a row in the diamond pattern.

Example:

Input: 3
Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
"""

n=5


lst=[]

# Pyramid Pattern
for i in range(n-1):
  str=""
  spc=""
  Nspace=(n-i)-1
  Nstar=(i*2)+1
  spc+=" " * Nspace
  str+="*" * Nstar
  lst.append(spc+str+spc)

# reverse Pyramid Pattern
for i in range(n):
  str=""
  spc=""
  NStar=(2*(n-i))-1
  spc+=" " * i
  str+="*" * NStar
  lst.append(spc+str+spc)

print(lst)

