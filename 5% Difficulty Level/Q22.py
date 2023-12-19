def calculateIndex():
    a, b = 1, 1
    fibList = [a, b]
    while True:
        a, b = b, a + b
        fibList.append(a+b)
        if len(str(a + b)) == 1000:
            break
    return(fibList.index(a+b) + 2)


print(calculateIndex())

# Answer: 4782
