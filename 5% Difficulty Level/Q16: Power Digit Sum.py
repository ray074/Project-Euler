def findSum():
    result = 2**1000
    resultList = list(str(result))
    return sum(int(x) for x in resultList)

print(findSum())

# Answer: 1366
