# URI ONLINE JUDGE ##############################################
# PROBLEM: 1012 - Area
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

A, B, C = input().split()

a = float(A)
b = float(B)
c = float(C)

pi = 3.14159

tri = a*c/2
cir = pi*(c**2)
tra = (a+b)*c/2
sqr = b**2
rec = a*b


print("TRIANGULO: %.3f" % tri)
print("CIRCULO: %.3f" % cir)
print("TRAPEZIO: %.3f" % tra)
print("QUADRADO: %.3f" % sqr)
print("RETANGULO: %.3f" % rec)