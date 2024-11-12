# Your code here
def factorial(num):
    total = 1
    for x in range(num, 1, -1):
        total *= x

    return total

result = factorial(4)

print(result)
