from math import factorial

def findSum():
    result = factorial(100)
    total = sum(int(x) for x in list(str(result)))
    return total

print(findSum())

# Answer: 648
