# URI ONLINE JUDGE ##############################################
# PROBLEM: 1015 - Distance Between Two Points
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

X1, Y1 = input().split()
X2, Y2 = input().split()

x1 = float(X1)
y1 = float(Y1)
x2 = float(X2)
y2 = float(Y2)


distance = ( (x2-x1)**2 + (y2-y1)**2 ) ** (1/2)

print("%.4f" % distance)