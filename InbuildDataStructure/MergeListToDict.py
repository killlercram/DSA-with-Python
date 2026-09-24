"""Merge Lists to Dictionary

Design a Python function named merge_lists_to_dictionary to merge two lists into a dictionary where elements from the first list act as keys and elements from the second list act as values.

Parameters:

keys (List): A list of keys.

values (List): A list of values.

Returns:

A dictionary containing merged key-value pairs.

Example:

Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}

Input: keys = ['x', 'y', 'z'], values = [10, 20, 30]
Output: {'x': 10, 'y': 20, 'z': 30}"""

# This is good but we have to take care of different lengths 
# def merge_lists_to_dictionary(keys, values):
#   result = {}

#   for i in range(len(keys)):
#     result[keys[i]] = values[i]

#   return result

# So we will be using Zip here which is more important

def merge_lists_to_dictionary(keys,values):
  if len(keys) != len(values):
    return False
  
  return dict(zip(keys , values))

print(merge_lists_to_dictionary(
    ['a', 'b', 'c'],
    [1, 2]
))