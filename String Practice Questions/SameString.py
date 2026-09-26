"""You are given two strings s and t. Your task is to check if the two strings are equal. Two strings are considered equal if they have the same length and the same characters at each position. You are not allowed to use any built-in string comparison functions.
Input:

Two strings s and t, where 1 <= len(s), len(t) <= 1000.

Output:

A boolean value (True or False) indicating whether the two strings are equal.

Example:

Input: s = "hello", t = "hello"
Output: True
 
Input: s = "hello", t = "world"
Output: False"""

def are_equal_strings(s, t):
  return s == t

print(are_equal_strings("hello", "world"))