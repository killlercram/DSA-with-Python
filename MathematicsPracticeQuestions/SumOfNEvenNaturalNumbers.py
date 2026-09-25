"""
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
"""
def sum_of_even_numbers(n):
  sum=0
  TotalSum = 0
  for i in range(0,n):
    sum+=2
    TotalSum+=sum
  return TotalSum


   

print(sum_of_even_numbers(5))
