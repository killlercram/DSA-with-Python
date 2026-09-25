"""
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
"""
from math import sqrt
def is_perfect_square(num):
  numCheck = sqrt(num)

  if numCheck.is_integer():
    return True

  return False

print(is_perfect_square(16))
