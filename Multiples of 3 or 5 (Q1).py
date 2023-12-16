def calculateSum():
    validNums = [num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0]
    return sum(validNums)

print(calculateSum())

# Answer: 233168
