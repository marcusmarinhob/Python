import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

varInterger = 12                  # interger
varFloat    = 21.11               # float
varString   = "Hello, World!"     # string 

print("Interger: " + str(varInterger))
print("Float: " + str(varFloat))
print("String: " +varString)


# Auto git saving #####################################################
save = 1
commitMsg = '1. Values and Data Types.' 

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
