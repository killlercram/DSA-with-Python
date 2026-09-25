def is_prime(n):
  numbers = 0
  for i in range(1,n+1):
    if n%i==0:
      numbers+=1

  if numbers > 2:
    return False;

  return True

print(is_prime(12))

