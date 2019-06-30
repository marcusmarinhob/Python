# URI ONLINE JUDGE ##############################################
# PROBLEM: 1020 - Age in Days
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

ageDays = int(input())

years = ageDays/365
months = (ageDays%365)/30
days = (ageDays%365)%30

print("%d ano(s)" % years)
print("%d mes(es)" % months)
print("%d dia(s)" % days)
