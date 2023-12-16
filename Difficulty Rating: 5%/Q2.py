def calculateEvenFibNums(limit=4000000):
    a, b, evens = 1, 2, [2]
    while a + b < limit:
        evens.append(a + b) if (a + b) % 2 == 0 else 0
        a, b = b, a + b
    return sum(evens)

print(calculateEvenFibNums())

# Answer: 4613732
