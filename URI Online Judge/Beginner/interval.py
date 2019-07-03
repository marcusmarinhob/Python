# URI ONLINE JUDGE ##############################################
# PROBLEM: 1037 - Interval
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

number = float(input())



if number < 0 or number > 100:
    print("Fora de intervalo")
else:
    if number>=0.00 and number<=25.00:
        intervalo = "[0,25]"
    elif number>25.00 and number<=50.00:
        intervalo = "(25,50]"
    elif number>50.00 and number<=75.00:
        intervalo = "(50,75]"
    elif number>75.00 and number<=100.00:
        intervalo = "(75,100]"

    print("Intervalo %s" % intervalo)