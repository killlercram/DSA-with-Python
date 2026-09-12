"""Problem Description:

You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', where the first row contains n stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be left-aligned.
Input:

A single integer n, where 1 <= n <= 100.

Output:

A list of strings where each string represents a row in the hollow inverted right-angled triangle.

Example:

Input: 4
Output: ['****', '* *', '**', '*']
 
Input: 5
Output: ['*****', '*  *', '* *', '**', '*']
"""

n=4

lst = []
for i in range(n,0,-1):
  if(i==n):
    lst.append("*" * n)
  elif(i==1):
    lst.append("*")
  else:
    lst.append("*" + " " * (i-2) + "*")

print(lst)
