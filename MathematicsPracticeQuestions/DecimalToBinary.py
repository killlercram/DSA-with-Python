"""
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
"""

def int_to_binary(n):
  # if n == 0:
  #   return "0"
  # Str = ""
  # m=n
  # if n<0:
  #   n*=-1
    

  # while n >= 1:
  #   rem = n % 2
  #   n = n//2
  #   Str+=str(rem)

  # Str = Str[::-1]
  # if m<0:
  #   newStr="-"
  #   newStr+=Str
  #   return newStr


  # return Str

  if n == 0:
    return "0"

  negative = n < 0
  n = abs(n)
  Str = ""

  while n>=1:
    Str+=str(n%2)
    n//=2

  Str = Str[::-1]

  return "-"+Str if negative else Str

print(int_to_binary(-6))

