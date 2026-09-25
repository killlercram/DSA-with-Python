"""
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
"""

def binary_to_decimal(binary_str):
  if not binary_str:
    return 0
  power = 0
  decimal = 0
  num = int(binary_str)
  while num >= 1:
    lastNum = num%10
    num//=10
    decimal+=(lastNum*(2**power))
    power+=1

  return decimal


print(binary_to_decimal("101"))
