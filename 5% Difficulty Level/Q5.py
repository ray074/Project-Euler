def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple():
    result = 1
    for i in range(1, 21):
        result = lcm(result, i)
    return result

print(smallest_multiple())

# Answer: 232792560
