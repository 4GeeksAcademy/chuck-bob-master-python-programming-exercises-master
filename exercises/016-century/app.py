import math
# Complete the function to return the respective number of the century
def century(year):
  return int(math.ceil(year / 100))


# Invoke the function with any given year
print(century(1234))
