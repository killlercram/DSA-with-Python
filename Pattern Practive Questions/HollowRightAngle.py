"""Problem Description:

You are given an integer n. Your task is to return a hollow right-angled triangle pattern of '*', where the first and last rows contain stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be right-aligned.

Input:

A single integer n, where 1 <= n <= 100.


Output:

A list of strings where each string represents a row in the hollow right-angled triangle.

Example:

Input: 4
Output: ['*', '**', '* *', '****']
 
Input: 5
Output: ['*', '**', '* *', '*  *', '*****']
"""
n=5

lst = []
for i in range(1, n + 1):
 if i == 1:
  lst.append("*")
 elif i == n:
  lst.append("*" * n)
 else:
  lst.append("*" + " " * (i - 2) + "*")

print(lst)



