"""You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) in the string and return the total count.

Input:

A single string s, where the length of s is between 1 and 1000.

Output:

An integer representing the total count of vowels in the input string.

Example:

Input: "Hello, World!"
Output: 3
 
Input: "Python Programming"
Output: 4"""

def count_vowels(s):
  # vowels = 0
  # for i in s:
  #   if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
  #     vowels+=1

  vowels ="aeiouAEIOU"
  vowel = 0
  for char in s:
    if char in vowels:
      vowel+=1

  return vowel

print(count_vowels("Python Programming"))
      