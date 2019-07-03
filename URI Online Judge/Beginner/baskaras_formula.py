# URI ONLINE JUDGE ##############################################
# PROBLEM: 1036 - Bhaskara's Formula
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

A,B,C = input().split()

a=float(A)
b=float(B)
c=float(C)

delta = (b**2) - 4*a*c

if (delta < 0) or (a == 0):
    print("Impossivel calcular")
else:
    R1 = (-b + delta**(1/2))/(2*a)
    R2 = (-b - delta**(1/2))/(2*a)

    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)