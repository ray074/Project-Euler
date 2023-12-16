def isPalindromic(num):
    return str(num) == str(num)[::-1]

def calculateLargestPalindrome():
    palindromes = []
    
    for x in range(100, 1000):
        for y in range(100, 1000):
            if isPalindromic(x * y):
                palindromes.append(x * y)
    
    return max(palindromes)

print(calculateLargestPalindrome())

# Answer: 906609
