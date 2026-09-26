"""
You are given two strings s and t. Your task is to determine if string t is a subsequence of string s. A subsequence of a string is a new string that is formed from the original string by deleting some (or no) characters without changing the order of the remaining characters.

Input:

Two strings s and t where the length of s is between 1 and 1000, and the length of t is between 1 and 1000.

Output:

Return True if t is a subsequence of s, and False otherwise.

Example:

Input: s = "abcde", t = "ace"
Output: True
 
Input: s = "abcde", t = "aec"
Output: False
"""

def is_subsequence(s, t):
  j=0
  for char in s:
    if j < len(t) and char == t[j]:
      j+=1

  return j == len(t)

print(is_subsequence("abcde","aec"))
    


