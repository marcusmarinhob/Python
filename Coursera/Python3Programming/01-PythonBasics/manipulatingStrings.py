import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

s1 = "Double quotes"
s2 = 'Single quotes'

m1 = '''
multiple lines - line 1
line 2
line 3'''

print(s1)
print(s2)
print(m1)


# Auto git saving #####################################################
save = 1 
commitMsg = '1. Manipulating Strings' 

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
