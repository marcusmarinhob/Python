# URI ONLINE JUDGE ##############################################
# PROBLEM: 1009 - Salary with Bonus
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

seller = input()
fixedSalary = float(input())
totalSales = float(input())

salary = fixedSalary + 0.15*totalSales

print("TOTAL = R$ %.2f" % salary)