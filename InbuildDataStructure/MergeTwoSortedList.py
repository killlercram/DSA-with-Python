"""
Merge Two Sorted Lists

You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted list. The resulting list should also be in non-decreasing order.

Parameters:

list1 (List of integers): The first sorted list.

list2 (List of integers): The second sorted list.

Returns:

A single list of integers, containing all elements from list1 and list2, sorted in non-decreasing order.

Example:

Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Input: list1 = [1, 4, 7], list2 = [2, 3, 5, 8]
Output: [1, 2, 3, 4, 5, 7, 8]
"""

def merge_two_sorted_lists(list1, list2):
  MergedList = []
  j=0
  i=0
  while i < len(list1) and  j < len(list2):
    if list1[i] < list2[j]:
      MergedList.append(list1[i])
      i+=1
    elif list1[i] == list2[j]:
      MergedList.append(list2[j])
      i+=1
      j+=1
    else:
      MergedList.append(list2[j])
      j+=1

  # for k in list1:
  #   if k  not in MergedList: 
  #     MergedList.append(k)

  while i < len(list1):
    MergedList.append(list1[i])
    i+=1

  # for k in list2:
  #   if k not in MergedList:
  #     MergedList.append(k)

  while j < len(list2):
      MergedList.append(list2[j])
      j+=1

  

  return MergedList

print(merge_two_sorted_lists([1, 4, 7], [2, 3, 5, 8]))