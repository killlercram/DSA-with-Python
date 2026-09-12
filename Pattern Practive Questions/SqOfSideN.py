"""
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
      """

def generate_square(n,lst):
    # Your code here
    for x in range(n):
        str=""
        for y in range(n):
          str+="*"

        lst.append(str)



          

lst =[]
generate_square(5,lst)
print(lst)
