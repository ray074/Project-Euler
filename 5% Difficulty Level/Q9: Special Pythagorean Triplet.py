def findSpecialPyTriplet():
    
    valid = set()

    for a in range(3, 2000):
        for b in range(3, 2000):
            c = sqrt(a**2 + b**2)
            if c.is_integer() and a < b < c:
                valid.add((a, b, int(c)))

    for triple in valid:
        if sum(triple) == 1000:
            total = 1
            for num in triple:
                total *= num
            return total
    
print(specialPyTriplet())

# Answer: 31875000
