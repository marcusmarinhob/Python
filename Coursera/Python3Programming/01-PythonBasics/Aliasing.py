import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

alist = [4,2,8,6,5]
blist = alist
blist[3] = 999
print(alist)




# Auto git saving #####################################################
save = 1
commitMsg = '1. Aliasing' 

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
