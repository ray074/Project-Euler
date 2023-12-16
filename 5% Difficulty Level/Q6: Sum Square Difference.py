def calculateDifference():
    total1, total2, = 0, 0
    
    for num in range(1, 101):
        total1 += num ** 2
        total2 += num
        
    return (total2 ** 2) - total1

print(calculateDifference())

# Answer: 25164150
