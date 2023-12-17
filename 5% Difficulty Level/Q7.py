#Q7: 

def isPrime(num):
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True


primeList = [x for x in range(2, 200000) if isPrime(x)]
print(primeList[10000])

# Answer: 104743
