import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)



# Auto git saving #####################################################
save = 1
commitMsg = '1. Using with for Files' 

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
#print('\n'*15)
