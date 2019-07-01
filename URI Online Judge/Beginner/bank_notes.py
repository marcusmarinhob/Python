# URI ONLINE JUDGE ##############################################
# PROBLEM: 1018 - Banknotes
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

N = int(input())

ced100 = N/100
ced50 = (N%100)/50
ced20 = ((N%100)%50)/20
ced10 = (((N%100)%50)%20)/10
ced5 = ((((N%100)%50)%20)%10)/5
ced2 = (((((N%100)%50)%20)%10)%5)/2
ced1 = (((((N%100)%50)%20)%10)%5)%2


print("%d" % N)
print("%d nota(s) de R$ 100,00" % ced100)
print("%d nota(s) de R$ 50,00" % ced50)
print("%d nota(s) de R$ 20,00" % ced20)
print("%d nota(s) de R$ 10,00" % ced10)
print("%d nota(s) de R$ 5,00" % ced5)
print("%d nota(s) de R$ 2,00" % ced2)
print("%d nota(s) de R$ 1,00" % ced1)
