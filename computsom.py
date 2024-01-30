def computeMultiplesSum(n):
    if n < 0 or n > 1000:
        raise ValueError("n doit être compris entre 0 et 1000")
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            total += i
    return total

# Exemple d'utilisation
n = 100
result = computeMultiplesSum(n)
print(result)
