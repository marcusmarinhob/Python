import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

olypmicsfile = open("olympics.txt","r")

for new_line in olypmicsfile.readlines():
    values = new_line.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()




# Auto git saving #####################################################
save = 1
commitMsg = '1. readlines() method in for loop' 

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
