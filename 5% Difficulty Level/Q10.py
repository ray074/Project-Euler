def isPrime(num):
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False
    return True


primeList = [p for p in range(2, 2000000) if isPrime(p)]
print(sum(primeList))

# Answer: 142913828922
