import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

a = 10
b = 20

opSum = a + b            # Sum
opSub = a - b            # Subtraction
opMult = a * b           # Multiplication
opDiv = a / b            # Division

opTruncDiv = a // b      # Truncated Division
opMod = a % b            # Module

opExp = a ** b           # Exponentiation

print("a + b = " + str(opSum))
print("a - b = " + str(opSub))
print("a * b = " + str(opMult))
print("a / b = " + str(opDiv))
print("a // b = "+ str(opTruncDiv))
print("a % "+"b = "+ str(opMod))
print("a ** b = "+ str(opExp) )




# Auto git saving #####################################################
save = 1
commitMsg = '1. Operators and Operands.' 

if save:
    print('\nAUTO GIT SAVING...')
    
    fileName = os.path.basename(__file__)    

    os.system('git add '+ fileName)
    os.system('git commit -m '+'"'+commitMsg+'"')
    os.system('git push')

    print('\nFile Name: '+fileName)
    print('\nCommit Message: '+commitMsg)
    print('\nSAVED AND PUSHED!')


print('\n# END OF THE SCRIPT ###############################################')
print('\n'*15)
