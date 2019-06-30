# URI ONLINE JUDGE ##############################################
# PROBLEM: 1008 - Salary
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

employee = int(input())
hoursWorked = int(input())
salaryPerHour = float(input())

salary = salaryPerHour * hoursWorked

print("NUMBER =", employee)
print("SALARY = U$ %.2f" % salary)