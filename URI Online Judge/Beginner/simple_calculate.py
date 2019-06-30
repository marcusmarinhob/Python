# URI ONLINE JUDGE ##############################################
# PROBLEM: 1010 - Simple Calculate
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

x, y, z  = input().split()
code1 = int(x)
numberOfUnits1=int(y)
price1= float(z)

x, y, z  = input().split()
code2 = int(x)
numberOfUnits2=int(y)
price2= float(z)

valueToPay = numberOfUnits1*price1 + numberOfUnits2*price2

print('VALOR A PAGAR: R$ %.2f' %valueToPay)