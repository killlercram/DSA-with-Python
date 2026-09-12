"""Problem Description:

You are given an integer n. Your task is to return a pyramid pattern of numbers, where each row contains increasing numbers starting from 1 up to the row number, and the pyramid is centered with leading spaces.

Input:

A single integer n, where 1 <= n <= 100.

Output:

A list of strings where each string represents a row in the pyramid pattern.

Example:

Input: 4
Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
 
Input: 3
Output: ['  1  ', ' 1 2 ', '1 2 3']
"""
n = 3

lst = []

for i in range(1, n + 1):
    str1 = []

    for j in range(1, i + 1):
        str1.append(str(j))

    row = " ".join(str1)
    row = row.center(2 * n - 1)

    lst.append(row)

print(lst)

