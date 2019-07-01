# URI ONLINE JUDGE ##############################################
# PROBLEM: 1017 - Fuel Spent
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

consumption = 12 #Km/l

spentTime = float(input()) #hours
avgSpeed = float(input()) #Km/l

dist = spentTime * avgSpeed

liters = dist/ consumption

print("%.3f" % liters)
