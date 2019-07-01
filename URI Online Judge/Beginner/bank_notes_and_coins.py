# URI ONLINE JUDGE ##############################################
# PROBLEM: 1021 - Banknotes and Coins
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

N = float(input())

ced100 = N/100
ced50 = (N%100)/50
ced20 = ((N%100)%50)/20
ced10 = (((N%100)%50)%20)/10
ced5 = ((((N%100)%50)%20)%10)/5
ced2 = (((((N%100)%50)%20)%10)%5)/2

coin1 =  (((((N%100)%50)%20)%10)%5)%2/1
coin50 = (((((((N%100)%50)%20)%10)%5)%2)%1)/0.5
coin25 = ((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)/0.25
coin10 = (((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)/0.1
coin05=  ((((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.1)/0.05
coin01=  round((((((((((((N%100)%50)%20)%10)%5)%2)%1)%0.5)%0.25)%0.1)%0.05)/0.01)


print("%s" % "NOTAS:")
print("%d nota(s) de R$ 100.00" % ced100)
print("%d nota(s) de R$ 50.00" % ced50)
print("%d nota(s) de R$ 20.00" % ced20)
print("%d nota(s) de R$ 10.00" % ced10)
print("%d nota(s) de R$ 5.00" % ced5)
print("%d nota(s) de R$ 2.00" % ced2)

print("%s" % "MOEDAS:")
print("%d moeda(s) de R$ 1.00" % coin1)
print("%d moeda(s) de R$ 0.50" % coin50)
print("%d moeda(s) de R$ 0.25" % coin25)
print("%d moeda(s) de R$ 0.10" % coin10)
print("%d moeda(s) de R$ 0.05" % coin05)
print("%d moeda(s) de R$ 0.01" % coin01)

