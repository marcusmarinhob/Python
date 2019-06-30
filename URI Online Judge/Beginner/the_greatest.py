# URI ONLINE JUDGE ##############################################
# PROBLEM: 1013 - The Greatest
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

A, B, C = input().split()

a = int(A)
b = int(B)
c = int(C)

pi = 3.14159

maiorAB = (a + b + abs(a-b))/2
maior = (c + maiorAB + abs(c - maiorAB))/2


print("%d eh o maior" % maior)
