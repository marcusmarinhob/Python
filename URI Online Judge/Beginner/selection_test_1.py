# URI ONLINE JUDGE ##############################################
# PROBLEM: 1035 - Selection Test 1
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

A, B, C, D = input().split()

a= int(A)
b= int(B)
c= int(C)
d= int(D)

if (b > c) and (d > a) and ((c+d)>(b+a)) and (c>0) and (d>0) and (a%2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
