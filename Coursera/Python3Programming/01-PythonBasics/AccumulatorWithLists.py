import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

list= [3,0,9,4,1,7]
new_list=[]
for i in range(len(list)):
   new_list.append(list[i]+5)
print(new_list)





# Auto git saving #####################################################
save = 1
commitMsg = '1. The Accumulator Pattern with Lists' 

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
