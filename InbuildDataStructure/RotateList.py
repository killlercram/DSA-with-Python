"""Rotate a List (Without Slicing)

You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions without using slicing. A rotation shifts elements from the end of the list to the front.

Parameters:

lst (List of integers): The list to be rotated.

k (Integer): The number of positions to rotate the list.

Returns:

A list of integers rotated by k positions.

Example:

Input: lst = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Input: lst = [10, 20, 30, 40, 50], k = 3
Output: [30, 40, 50, 10, 20]"""

def rotate_list(lst, k):
  if len(lst) <= 0: # we can write it as if not lst:
    return lst

  k = k%len(lst)
  i = len(lst) - k
  newList = []
  
  
  for j in range(i,len(lst)):
    newList.append(lst[j])

  for j in range(0,i):
    newList.append(lst[j])

  return newList


print(rotate_list([1, 2, 3, 4, 5],7))

# We can also use reversal Algo
# we can reverse all the element in the list 
# Now we can reverse the first k element
# Then now we can reverse the other half of the elements
