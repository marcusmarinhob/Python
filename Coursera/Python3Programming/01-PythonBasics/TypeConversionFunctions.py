import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

print("int(",3.14,") =", int(3.14))
print("float(","123.45",") =", float("123.45"))
print("str(",3.14,") =", str(3.14))


val = 50 + 5
print("The value is " + str(val))


# Auto git saving #####################################################
save = 1
commitMsg = '1. Type Conversion Functions.' 

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
print('\n'*3)
