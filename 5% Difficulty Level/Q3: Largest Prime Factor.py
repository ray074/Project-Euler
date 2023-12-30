def isPrime(num):
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False
    return True


num = 600851475143
print(max([x for x in range(2, int(num ** 0.5) + 1) if num % x == 0 and isPrime(x)]))

# Answer: 6857
