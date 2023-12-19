from names import names

def calculateScore(names):
    names = sorted(names)
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    score = 0
   
    for pos, name in enumerate(names):
        total = 0
        for char in list(name):
            total += alpha.index(char) + 1
       
        score += total * (pos + 1)
        return score

print(calculateScore(names))

# Answer: 871198282
