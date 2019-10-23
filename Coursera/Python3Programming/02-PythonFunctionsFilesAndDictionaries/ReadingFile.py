import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

fileref = open("olympics.txt","r")

num_char = len(fileref.read()) # Reads and returns a string of n characters, 
                               # or the entire file as a single string if n 
                               # is not provided.

fileref.close()





# Auto git saving #####################################################
save = 1
commitMsg = '1. read() method' 

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
