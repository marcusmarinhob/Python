# URI ONLINE JUDGE ##############################################
# PROBLEM: 1019 - Time Conversion
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

N = int(input())

h = N/3600
m = (N%3600)/60
s = (N%3600)%60

print("%d:%d:%d" %(h, m, s))
