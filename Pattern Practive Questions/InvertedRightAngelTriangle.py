"""
Problem Description:

You are given an integer n. Your task is to return an inverted right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The first row should have n stars, the second row n-1 stars, and so on, until the last row has 1 star.

Input Parameters:

n (int): The height and base of the inverted right-angled triangle.

Output:

A list of strings where each string is a row of '*' characters that decreases in length from n to 1.

Example:

Input: 3
Output: ['***', '**', '*']
 
Input: 5
Output: ['*****', '****', '***', '**', '*']

"""


n=5

# lst=[]
# for i in range(n):
#   str=""
#   for j in range(n-i,0,-1):
#     str+="*"
#   lst.append(str)

# print(lst)


# Simpler Python way of doing it without using nested loop
lst = []
for i in range(n,0,-1):
  str=""
  str+=("*" * i)
  lst.append(str)

print(lst)




