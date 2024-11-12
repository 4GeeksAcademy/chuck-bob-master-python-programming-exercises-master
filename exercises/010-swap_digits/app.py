# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here

  tens_to_ones =  num // 10
  ones_to_tens = num % 10 * 10
   
  return tens_to_ones+ones_to_tens

# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
