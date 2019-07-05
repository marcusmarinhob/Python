# URI ONLINE JUDGE ##############################################
# PROBLEM: 1259 - Even and Odd
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################


forIndex = int(input())

even = []
odd = []

for index in range(0, forIndex):
    number = int(input())
    
    if number%2 == 0:
        even.append(number)
    else:
        odd.append(number)

even.sort()
odd.sort(reverse = True)

for num in even:
    print(num)

for num in odd:
    print(num)